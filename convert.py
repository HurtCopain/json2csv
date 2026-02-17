import pandas as pd
import glob
import os

# Find all files starting with 'dataset' or ending in '.json'
json_files = glob.glob("dataset*") + glob.glob("*.json")
json_files = list(set(json_files))

if not json_files:
    print("No JSON files found in the current directory.")
else:
    for file in json_files:
        try:
            print(f"Processing {file}...")
            # lines=True handles the 'Extra Data' / NDJSON format
            df = pd.read_json(file, lines=True)
            
            # Generate output filename
            csv_filename = f"{os.path.splitext(file)[0]}.csv"
            
            # Export to CSV
            df.to_csv(csv_filename, index=False, encoding='utf-8')
            print(f"Successfully created {csv_filename}")
        except Exception as e:
            print(f"Error processing {file}: {e}")

print("\nBatch conversion complete!")
