#!/usr/bin/env python3
"""DataFlow - Fast CSV/JSON data processor and converter"""
import json
import csv
import sys
import argparse
from pathlib import Path

def process_csv_to_json(csv_path):
    """Convert CSV to JSON"""
    with open(csv_path) as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return json.dumps(data, indent=2)

def process_json_to_csv(json_path):
    """Convert JSON to CSV"""
    with open(json_path) as f:
        data = json.load(f)
    
    if not data:
        return ""
    
    if isinstance(data, list) and isinstance(data[0], dict):
        fieldnames = data[0].keys()
        output = []
        writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
        return None
    return ""

def validate_json(json_path):
    """Validate JSON file"""
    try:
        with open(json_path) as f:
            json.load(f)
        return True, "Valid JSON"
    except json.JSONDecodeError as e:
        return False, f"Invalid JSON: {e}"

def main():
    parser = argparse.ArgumentParser(description="DataFlow - CSV/JSON processor")
    parser.add_argument("input", help="Input file (CSV or JSON)")
    parser.add_argument("--output", "-o", help="Output file (optional)")
    parser.add_argument("--format", "-f", choices=["csv", "json"], help="Output format")
    parser.add_argument("--validate", "-v", action="store_true", help="Validate JSON")
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: {args.input} not found", file=sys.stderr)
        sys.exit(1)
    
    suffix = input_path.suffix.lower()
    
    if args.validate and suffix == ".json":
        valid, msg = validate_json(args.input)
        print(msg)
        sys.exit(0 if valid else 1)
    
    output_format = args.format or ("json" if suffix == ".csv" else "csv")
    
    try:
        if suffix == ".csv" and output_format == "json":
            result = process_csv_to_json(args.input)
        elif suffix == ".json" and output_format == "csv":
            result = process_json_to_csv(args.input)
        else:
            print(f"Error: Cannot convert {suffix} to {output_format}", file=sys.stderr)
            sys.exit(1)
        
        if result is not None:
            if args.output:
                with open(args.output, "w") as f:
                    f.write(result)
                print(f"Wrote to {args.output}")
            else:
                print(result)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
