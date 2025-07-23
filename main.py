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

    qr = qrcode.make(url)
    buffer = io.BytesIO()
    qr.save(buffer, format="PNG")
    base64_img = base64.b64encode(buffer.getvalue()).decode("utf-8")
    print(base64_img)

if __name__ == "__main__":
    main()
