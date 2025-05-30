import qrcode
import os

BASE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfC-T-H0c96gLrpmAm8_Y-A2k63WTVaKiQJjrYaihNlgiW0-g/viewform"
ENTRY_FIELD = "entry.1071820856" # Replace with actual entry ID for Tree ID

QR_OUTPUT_DIR = "static/images/qr"

def generate_prefilled_url(tree_id):
    return f"{BASE_FORM_URL}?{ENTRY_FIELD}={tree_id}"

def generate_qr_code(tree_id):
    if not os.path.exists(QR_OUTPUT_DIR):
        os.makedirs(QR_OUTPUT_DIR)

    prefilled_url = generate_prefilled_url(tree_id)
    img = qrcode.make(prefilled_url)
    file_path = os.path.join(QR_OUTPUT_DIR, f"{tree_id}.png")
    img.save(file_path)
    return tree_id, prefilled_url, file_path

# Example usage
if __name__ == "__main__":
    sample_tree_ids = ["TREE01", "TREE02", "TREE03"]
    for tree_id in sample_tree_ids:
        path = generate_qr_code(tree_id)
        print(f"Generated QR for {tree_id} -> {path}")