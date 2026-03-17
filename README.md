# DataFlow — Fast CSV/JSON Data Processor

Convert, validate, and transform CSV and JSON files instantly.

## Features
- **CSV ↔ JSON conversion** — switch formats in seconds
- **JSON validation** — catch syntax errors fast
- **CLI-based** — integrate into pipelines
- **Zero dependencies** — pure Python, works everywhere

## Installation
```bash
chmod +x dataflow.py
./dataflow.py --help
```

## Usage
```bash
# CSV to JSON
./dataflow.py data.csv --format json --output data.json

# JSON to CSV
./dataflow.py data.json --format csv --output data.csv

# Validate JSON
./dataflow.py data.json --validate

# Print to stdout
./dataflow.py data.csv --format json
```

## Examples
```bash
# Process a file
./dataflow.py sales.csv -f json -o sales.json

# Quick validation
./dataflow.py config.json -v

# Pipe to other tools
./dataflow.py raw.csv -f json | jq '.[] | select(.status=="active")'
```

## Use Cases
- **Data pipeline automation** — batch convert formats in scripts
- **API integration** — transform data formats for different endpoints
- **ETL workflows** — lightweight data transformation
- **Configuration management** — convert config formats

Simple. Fast. Works.
