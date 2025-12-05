# ir_tool/analyzer.py
from whoosh.analysis import (
    RegexTokenizer,
    LowercaseFilter,
    StopFilter,
    Filter,
    CompositeAnalyzer,
)
from nltk.corpus import stopwords
from nltk.stem.snowball import GermanStemmer

class GermanSnowballFilter(Filter):
    def __init__(self):
        self.stemmer = GermanStemmer()
    def __call__(self, stream):
        for t in stream:
            t.text = self.stemmer.stem(t.text)
            yield t

def test_analyzer(text: str, analyzer: CompositeAnalyzer):
    tokens = [token.text for token in analyzer(text)]
    print(tokens)

def german_text_analyzer():
    stop = set(stopwords.words("german"))
    return (RegexTokenizer() 
            | LowercaseFilter() 
            | StopFilter(stop)
            | GermanSnowballFilter())

def simple_analyzer():
    return (RegexTokenizer()
            | LowercaseFilter()
            | StopFilter())
