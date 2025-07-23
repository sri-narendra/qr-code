# main.py

import sys
import json
import qrcode
import io
import base64

def main():
    try:
        input_data = json.load(sys.stdin)
    except Exception as e:
        print(f"Error reading input: {e}", file=sys.stderr)
        exit(1)

    url = input_data.get("url")
    if not url:
        print("Error: URL is required", file=sys.stderr)
        exit(1)

    try:
        img = qrcode.make(url)
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        base64_img = base64.b64encode(buf.getvalue()).decode()
        print(base64_img)  # ✅ This is what's returned
    except Exception as e:
        print(f"QR generation failed: {e}", file=sys.stderr)
        exit(1)

if __name__ == "__main__":
    main()
