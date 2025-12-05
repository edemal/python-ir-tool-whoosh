# ir_tool/schema.py
from whoosh.fields import Schema, TEXT, ID
from .analyzer import simple_analyzer

def make_schema():
    # path: zum Anzeigen, contents: durchsuchbares Feld
    return Schema(
        path=ID(stored=True, unique=True),
        contents=TEXT(stored=True, analyzer=simple_analyzer()),
        # TODO: Use JSON schema of covid-19 articles here
        # https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/2020-03-13/json_schema.txt
    )