# ir_tool/cli.py
from pathlib import Path
import typer, json
from .indexing import build_index
from .searching import search
from .analyzer import test_analyzer as ta

app = typer.Typer()

@app.command()
def index(collection: Path = typer.Argument(..., help="Ordner mit .txt-Dateien"),
          out: Path = typer.Argument(Path("index"), help="Index-Ordner")):
    build_index(collection, out)
    typer.echo(f"Index erstellt unter: {out}")

@app.command()
def query(idx: Path = Path("index"),
          q: str = typer.Argument(..., help="Query, z.B. \"künstliche intelligenz\""),
          limit: int = 20,
          wildcard: bool = False):
    results = search(idx, q, limit=limit, wildcard=wildcard)
    for r in results:
        typer.echo(f"[{r['score']:.3f}] {r['path']}\n  {r['snippet']}\n")

@app.command()
def query_json(idx: Path = Path("index"), q: str = typer.Argument(...), limit: int = 20, wildcard: bool = False):
    typer.echo(json.dumps(search(idx, q, limit=limit, wildcard=wildcard), ensure_ascii=False, indent=2))

@app.command()
def test_analyzer(text: str = typer.Argument(..., help="Text zum Analysieren")):
    ta(text)

if __name__ == "__main__":
    app()