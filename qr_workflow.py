from sheets_api import fetch_tree_ids, append_qr_row
from qr_generator import generate_prefilled_url, generate_qr_code
from drive_api import upload_file_to_drive

def process_all_tree_ids():
    tree_ids = fetch_tree_ids()
    print(f"Fetched {len(tree_ids)} Tree IDs")

    for tree_id in tree_ids:
        print(f"Processing Tree ID: {tree_id}")

        # 1. Generate prefilled Google Form URL
        prefilled_url = generate_prefilled_url(tree_id)

        # 2. Generate QR code PNG file locally
        _, _, qr_file_path = generate_qr_code(tree_id)  # Unpack to get file path

        # 3. Upload PNG to Google Drive and get sharable URL
        qr_url = upload_file_to_drive(qr_file_path, tree_id)

        # 4. Append the data row to Google Sheet incrementally
        append_qr_row(tree_id, prefilled_url, qr_url)

        print(f"Appended data for {tree_id}")

if __name__ == "__main__":
    process_all_tree_ids()
