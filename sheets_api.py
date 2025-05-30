import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = "credentials/sa_key.json"
SPREADSHEET_ID = "13YQu0gbLLgar55plAP35M-ZsYoMz-DB2NaO1mc3kA7Q"
FETCH_RANGE = "Tree_ID!E2:E"  # Adjust as needed

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
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=FETCH_RANGE).execute()
    values = result.get('values', [])
    tree_ids = [row[0] for row in values if row]
    return tree_ids

def append_qr_row(tree_id, prefilled_url, qr_url):
    service = get_sheets_service()
    sheet = service.spreadsheets()

    values = [[tree_id, prefilled_url, qr_url]]

    body = {
        'values': values
    }

    sheet.values().append(
        spreadsheetId=SPREADSHEET_ID,
        range="QR_Codes!A2:C",
        valueInputOption="RAW",
        insertDataOption="INSERT_ROWS",
        body=body
    ).execute()

if __name__ == "__main__":
    tree_ids = fetch_tree_ids()
    print(f"Fetched Tree IDs: {tree_ids}")
