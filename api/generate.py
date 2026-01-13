import json
import qrcode
import base64
from io import BytesIO

def handler(request):
    try:
        body = json.loads(request.body)
        link = body.get("link")

        if not link:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "No link provided"})
            }

        qr = qrcode.make(link)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")

        img_base64 = base64.b64encode(buffer.getvalue()).decode()

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"image": img_base64})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }