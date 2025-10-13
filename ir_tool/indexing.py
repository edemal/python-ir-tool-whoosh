# ir_tool/indexing.py
from pathlib import Path
from whoosh import index
from .schema import make_schema

def build_index(collection_dir: Path, index_dir: Path) -> None:
    index_dir.mkdir(parents=True, exist_ok=True)
    if not index.exists_in(index_dir):
        ix = index.create_in(index_dir, make_schema())
    else:
        ix = index.open_dir(index_dir)

    writer = ix.writer()
    try:
        for p in collection_dir.rglob("*.txt"):
            text = p.read_text(encoding="utf-8", errors="ignore")
            writer.update_document(path=str(p.resolve()), contents=text)
    finally:
        writer.commit()