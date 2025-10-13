# ir_tool/schema.py
from whoosh.fields import Schema, TEXT, ID
from .analyzer import german_text_analyzer

def make_schema():
    # path: zum Anzeigen, contents: durchsuchbares Feld
    return Schema(
        path=ID(stored=True, unique=True),
        contents=TEXT(stored=True, analyzer=german_text_analyzer())
    )