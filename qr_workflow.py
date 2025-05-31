import argparse
from sheets_api import fetch_tree_ids, append_qr_row
from qr_generator import generate_prefilled_url, generate_qr_code
from drive_api import upload_file_to_drive

parser = argparse.ArgumentParser(description="Generate QR codes for a specific range of rows.")
parser.add_argument('--start', type=int, required=True, help="Start row (1-based index)")
parser.add_argument('--end', type=int, required=True, help="End row (inclusive, 1-based index)")
args = parser.parse_args()

start_idx = args.start - 1
end_idx = args.end

def process_all_tree_ids():
    tree_ids = fetch_tree_ids()
    print(f"Fetched {len(tree_ids)} Tree IDs")

    tree_ids = tree_ids[start_idx:end_idx]

    for tree_id in tree_ids:
        print(f"Processing Tree ID: {tree_id}")

        prefilled_url = generate_prefilled_url(tree_id)
        _, _, qr_file_path = generate_qr_code(tree_id)
        qr_url = upload_file_to_drive(qr_file_path, tree_id)
        append_qr_row(tree_id, prefilled_url, qr_url)

        print(f"Appended data for {tree_id}")

if __name__ == "__main__":
    process_all_tree_ids()

