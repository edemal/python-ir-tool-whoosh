# ir_tool/searching.py
from typing import Iterable
from whoosh import index
from whoosh.qparser import MultifieldParser, OrGroup, FuzzyTermPlugin, WildcardPlugin
from whoosh.query import Wildcard

def search(index_dir, query: str, limit: int = 20, wildcard: bool = False):
    ix = index.open_dir(index_dir)
    with ix.searcher() as s:
        # Parser (mehr Felder wären leicht erweiterbar)
        parser = MultifieldParser(["contents"], schema=ix.schema, group=OrGroup)
        parser.add_plugin(FuzzyTermPlugin())
        parser.add_plugin(WildcardPlugin())

        q = Wildcard("contents", query) if wildcard else parser.parse(query)
        results = s.search(q, limit=limit)
        results.fragmenter.charlimit = None  # saubere Snippets
        results.fragmenter.maxchars = 160
        results.formatter.tagname = "mark"

        out = []
        for hit in results:
            snippet = hit.highlights("contents", top=1) or ""
            out.append({"path": hit["path"], "score": float(hit.score), "snippet": snippet})
        return out