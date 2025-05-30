# Air4Four QR Code Generator

## Overview

This project automates the process of generating QR codes for Tree IDs, uploading the QR images to Google Drive, and appending related data to a Google Sheet. It integrates with Google Sheets API, Google Drive API, and uses a Google Form to collect information linked to the Tree IDs.

---

## Key Files and Their Roles

- **`sheets_api.py`**  
  Handles fetching Tree IDs from the Google Sheet and appending new rows incrementally to the QR_Codes sheet.

- **`qr_generator.py`**  
  Generates prefilled Google Form URLs and creates QR code PNG files locally for each Tree ID.

- **`drive_api.py`**  
  Uploads QR code PNG files to Google Drive and returns the shareable URL.

- **`process_tree_ids.py`**  
  Main script that orchestrates the workflow: fetches Tree IDs, generates URLs and QR codes, uploads files, and appends data back to Google Sheets.

- **`requirements.txt`**  
  Lists all Python dependencies needed to run the project.

---

## Full Workflow

1. **Fetch Tree IDs**  
   `process_tree_ids.py` calls `fetch_tree_ids()` from `sheets_api.py` to retrieve all Tree IDs from the source Google Sheet.

2. **Generate URLs and QR Codes**  
   For each Tree ID:  
   - Generate a prefilled Google Form URL (`qr_generator.py`)  
   - Create a QR code PNG file locally for that URL

3. **Upload QR Codes**  
   Upload each QR code PNG to Google Drive using `upload_file_to_drive()` in `drive_api.py`, retrieving a shareable URL.

4. **Append Data to Google Sheet**  
   Append a new row containing the Tree ID, prefilled form URL, and QR code URL to the "QR_Codes" sheet incrementally using `append_qr_row()` in `sheets_api.py`.

---

## Setup Instructions

1. **Install dependencies**  
   ```bash
   pip install -r requirements.txt

## How to Run

Run the main workflow script to process all Tree IDs, generate prefilled Google Form URLs, create QR codes, upload QR images to Google Drive, and append the data to the Google Sheet:

```bash
python3 qr_workflow.py


Let me know if you want me to add or tweak anything else!
