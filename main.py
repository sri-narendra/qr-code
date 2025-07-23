# main.py

import sys
import json
import qrcode
import io
import base64

def main():
    input_data = json.load(sys.stdin)
    url = input_data.get("url")

    if not url:
        print("Error: URL is required", file=sys.stderr)
        exit(1)

    img = qrcode.make(url)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    base64_img = base64.b64encode(buf.getvalue()).decode()
    print(base64_img)

if __name__ == "__main__":
    main()
