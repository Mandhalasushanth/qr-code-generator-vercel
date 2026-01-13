import qrcode
import base64
from io import BytesIO

def handler(request):
    data = request.json
    link = data.get("link")

    qr = qrcode.make(link)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")

    img_base64 = base64.b64encode(buffer.getvalue()).decode()

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": {
            "image": img_base64
        }
    }
