import sys
import json
try:
    import qrcode
    from qrcode.image.pil import PilImage
    import io
    import base64
except ImportError as e:
    print(f"ImportError: {str(e)}", file=sys.stderr)
    exit(1)

def generate_qr(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    return qr.make_image(fill_color="black", back_color="white")

def main():
    try:
        # Read input from stdin
        input_data = json.load(sys.stdin)
        url = input_data.get("url")
        
        if not url:
            print("Error: URL parameter is required", file=sys.stderr)
            exit(1)

        # Generate and convert to base64
        img = generate_qr(url)
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        base64_img = base64.b64encode(buffer.getvalue()).decode("utf-8")
        
        # Output must be printed
        print(base64_img)

    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        exit(1)

if __name__ == "__main__":
    main()
