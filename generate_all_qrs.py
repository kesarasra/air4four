# generate_all_qrs.py

from sheets_api import fetch_tree_ids
from qr_generator import generate_qr_code

def main():
    tree_ids = fetch_tree_ids()
    print(f"Found {len(tree_ids)} Tree IDs")

    for tree_id in tree_ids:
        path = generate_qr_code(tree_id)
        print(f"✅ Generated QR for {tree_id} at {path}")

if __name__ == "__main__":
    main()
