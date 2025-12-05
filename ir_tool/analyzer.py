# ir_tool/analyzer.py
from whoosh.analysis import RegexTokenizer, LowercaseFilter, StopFilter, Filter
from nltk.corpus import stopwords
from nltk.stem.snowball import GermanStemmer

class GermanSnowballFilter(Filter):
    def __init__(self):
        self.stemmer = GermanStemmer()
    def __call__(self, stream):
        for t in stream:
            t.text = self.stemmer.stem(t.text)
            yield t

def test_analyzer(text: str):
    analyzer = german_text_analyzer()
    tokens = [token.text for token in analyzer(text)]
    print(tokens)

def german_text_analyzer():
    german_stop = set(stopwords.words("german"))
    return (RegexTokenizer() 
            | LowercaseFilter() 
            | StopFilter(german_stop) 
            | GermanSnowballFilter())


