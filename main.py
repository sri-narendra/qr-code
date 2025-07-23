import sys
import json
import qrcode
import io
import base64

def main():
    try:
        # Read input from stdin
        input_data = json.load(sys.stdin)
        url = input_data.get("url")
        
        if not url:
            print("Error: URL is required", file=sys.stderr)
            exit(1)

        # Generate QR code
        qr = qrcode.make(url)
        buffer = io.BytesIO()
        qr.save(buffer, format="PNG")
        
        # Return as base64
        base64_img = base64.b64encode(buffer.getvalue()).decode("utf-8")
        print(base64_img)  # 👈 This print is CRITICAL

    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        exit(1)

if __name__ == "__main__":
    main()
