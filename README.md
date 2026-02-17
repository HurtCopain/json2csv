# JSON to CSV Converter (WSL Ubuntu) - Easily adjusted for any Debian flavor

A robust Python utility designed for WSL (Windows Subsystem for Linux) environments to batch-convert JSON or JSON Lines (NDJSON) files into flattened CSV spreadsheets.

## 🚀 Quick Start (WSL Terminal)

### 1. Setup Project Directory
Open your WSL Ubuntu terminal and create your workspace:
```bash
mkdir json_project && cd json_project

Configure Environment

# Install the venv tool
sudo apt update && sudo apt install python3-venv -y

# Create and activate the environment
python3 -m venv venv
source venv/bin/activate

Install Dependencies
sudo apt install python3 python3-pip python3-dev -y

Trust but verify
python3 --version
pip3 --version

pip install pandas

sudo apt update && sudo apt upgrade -y

🛠 Troubleshooting
"Externally Managed Environment" Error: Ensure you have activated the virtual environment using source venv/bin/activate.

JSONDecodeError: This script uses lines=True to handle files where each line is a separate JSON object. If your file is a standard single JSON array, the script is designed to catch and handle it.

Project Structure
json_project/
├── venv/             # Python virtual environment (hidden/ignored)
├── convert.py        # Main Python script
├── dataset1          # Input JSON file
└── dataset1.csv      # Generated output file

Run the Script
Place your dataset1, dataset2, etc., files in this folder and run:

python3 convert.py

Updated the script to include a FIELDS_TO_KEEP list.

If you leave the list empty, it will export everything (all columns).

If you add names to the list (e.g., ['CreationDate', 'UserId', 'ClientIP']), it will filter the CSV to only those specific columns.

To use the filter:

Open convert.py in your text editor (you can use nano convert.py in WSL).

Find the line: FIELDS_TO_KEEP = []

Change it to include the specific headers you care about. For example:
FIELDS_TO_KEEP = ['CreationTime', 'UserId', 'Operation', 'ClientIP', 'ObjectId']

Save and run the script.

Important Note on Column Names:
The names are case-sensitive. Since Microsoft uses PascalCase, make sure you match the exact spelling (e.g., ClientIP instead of clientip).

Why use existing_columns?
I added a safety check in the code (existing_columns). This ensures that if you ask for a column like ClientIP, but it doesn't exist in one of your datasets, the script won't crash—it will just skip that column and move on.
