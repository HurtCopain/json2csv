import pandas as pd
import json
import glob
import os

# --- CONFIGURATION ---
# Add column names here to filter the output. 
# Example: FIELDS_TO_KEEP = ['CreationTime', 'UserId', 'Operation', 'ClientIP']
FIELDS_TO_KEEP = [] 

def process_audit_logs(file_path):
    all_records = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            try:
                # 1. Parse the main JSON line
                record = json.loads(line)
                
                # 2. Deep Dive: Unpack nested stringified JSON
                keys_to_unpack = ['AuditData', 'ExtendedProperties']
                
                for key in keys_to_unpack:
                    if key in record and isinstance(record[key], str):
                        try:
                            nested_json = json.loads(record[key])
                            if isinstance(nested_json, dict):
                                record.update(nested_json)
                            del record[key]
                        except json.JSONDecodeError:
                            pass
                
                all_records.append(record)
                
            except Exception as e:
                print(f"Skipping a row in {file_path} due to error: {e}")

    # 3. Flatten the list into a DataFrame
    df = pd.json_normalize(all_records)

    # 4. Apply Filtering logic
    if FIELDS_TO_KEEP:
        existing_columns = [col for col in FIELDS_TO_KEEP if col in df.columns]
        df = df[existing_columns]
    
    return df

# --- Execution ---
json_files = list(set(glob.glob("dataset*") + glob.glob("*.json")))

if not json_files:
    print("No files found. Ensure dataset files are in this folder.")
else:
    for file in json_files:
        if file.endswith('.csv') or file.endswith('.py'):
            continue
            
        print(f"Deep-parsing {file}...")
        df = process_audit_logs(file)
        
        csv_filename = f"{os.path.splitext(file)[0]}_Detailed.csv"
        df.to_csv(csv_filename, index=False, encoding='utf-8')
        print(f"Done! Created {csv_filename} with {len(df.columns)} columns.")

print("\nBatch conversion complete!")
