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
