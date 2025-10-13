# Python IR Tool

This project is an information retrieval tool built with [Whoosh](https://whoosh.readthedocs.io/en/latest/). 

## Features

- Index and search documents 
- With german text analayzer

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install whoosh typer[all] nltk
python - <<'PY'
import nltk
nltk.download('stopwords')
PY
```

## Usage

### Build index
```bash
python -m ir_tool.cli index ./test-collection ./index
```

### Wildcard search 
```bash
python -m ir_tool.cli query "vide*" --wildcard
```

### 

## Documentation

For more information, see the [Whoosh documentation](https://whoosh.readthedocs.io/en/latest/).