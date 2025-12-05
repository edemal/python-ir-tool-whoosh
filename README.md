# Python IR Tool

Simple information retrieval tool built with [Whoosh](https://whoosh.readthedocs.io/en/latest/).

## Features

- Index and search json documents like the [COVID-19 Open Research Dataset (CORD-19)](https://github.com/allenai/cord19?tab=readme-ov-file).

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install whoosh "typer[all]" nltk
python - <<'PY'
import nltk
nltk.download('stopwords')
PY
```

## Preparing Data
Download and extract the [COVID-19 Open Research Dataset (CORD-19)](https://github.com/allenai/cord19?tab=readme-ov-file) to a local directory. Use the `noncomm_use_subset` folder for non-commercial use.

## Usage

### Build index
```bash
python -m ir_tool.cli index ./noncomm_use_subset ./index
```

### Wildcard search 
```bash
python -m ir_tool.cli query "body_text" --wildcard
```

### Test analyzer
```bash
python -m ir_tool.cli test-analyzer "This is a simple test" --analyzer simple
```

## Documentation

For more information, see the [Whoosh documentation](https://whoosh.readthedocs.io/en/latest/).