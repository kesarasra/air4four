import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Constants
SERVICE_ACCOUNT_FILE = 'credentials/sa_key.json'
SCOPES = ['https://www.googleapis.com/auth/drive']
FOLDER_ID = '1990QXKZWGnBmA1Aa55rs9pH6wjlwmLYA'  

def get_drive_service():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES
    )
    return build('drive', 'v3', credentials=credentials)

def upload_file_to_drive(file_path, tree_id):
    service = get_drive_service()

    file_metadata = {
        'name': f'{tree_id}.png',
        'parents': [FOLDER_ID]
    }
    media = MediaFileUpload(file_path, mimetype='image/png')
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    # Make file publicly viewable
    file_id = file.get('id')
    service.permissions().create(
        fileId=file_id,
        body={'role': 'reader', 'type': 'anyone'},
    ).execute()

    # Create sharable URL
    file_url = f"https://drive.google.com/uc?export=view&id={file_id}"
    return file_url

# Example usage
if __name__ == "__main__":
    test_path = "static/images/qr/N12KY01.png"
    url = upload_file_to_drive(test_path, "N12KY01")
    print(f"File uploaded and accessible at: {url}")
