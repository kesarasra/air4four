import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = "credentials/sa_key.json"
SPREADSHEET_ID = "1-L2izXLfLDq-JMQ4Z_h0svSYVqSlB-V77HyaWaFqWKE"
FETCH_TREE_IDS_RANGE = "Sheet1!E2:E"  # Adjust as needed
FETCH_QR_DATA_RANGE = "Sheet2!A2:C"   # The range for appended QR data

def get_sheets_service():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    service = build('sheets', 'v4', credentials=credentials)
    return service

def fetch_tree_ids():
    service = get_sheets_service()
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=FETCH_TREE_IDS_RANGE).execute()
    values = result.get('values', [])
    tree_ids = [row[0] for row in values if row]
    return tree_ids

def fetch_existing_qr_data():
    """
    Fetch existing QR data rows from Sheet2.
    Returns a dict: { tree_id: { 'prefilled_url': str, 'qr_url': str } }
    """
    service = get_sheets_service()
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=FETCH_QR_DATA_RANGE).execute()
    values = result.get('values', [])
    
    data = {}
    for row in values:
        # Defensive check, expect at least 3 columns: tree_id, prefilled_url, qr_url
        if len(row) >= 3:
            tree_id, prefilled_url, qr_url = row[0], row[1], row[2]
            data[tree_id] = {
                'prefilled_url': prefilled_url,
                'qr_url': qr_url
            }
    return data

def append_qr_row(tree_id, prefilled_url, qr_url):
    service = get_sheets_service()
    sheet = service.spreadsheets()

    values = [[tree_id, prefilled_url, qr_url]]

    body = {
        'values': values
    }

    sheet.values().append(
        spreadsheetId=SPREADSHEET_ID,
        range="Sheet2!A2:C",
        valueInputOption="RAW",
        insertDataOption="INSERT_ROWS",
        body=body
    ).execute()

if __name__ == "__main__":
    tree_ids = fetch_tree_ids()
    print(f"Fetched Tree IDs: {tree_ids}")

    existing_qr_data = fetch_existing_qr_data()
    print(f"Existing QR Data: {existing_qr_data}")
