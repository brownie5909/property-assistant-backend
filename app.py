from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Property Assistant API is running!"

@app.route("/generate-report", methods=["POST"])
def generate_report():
    data = request.get_json()
    if not data or "address" not in data:
        return jsonify({"error": "Missing address"}), 400

    address = data["address"]
    # Mock response
    return jsonify({
        "address": address,
        "summary": "This would be the PDF summary for the address.",
        "link": "https://drive.google.com/file/d/your-file-id/view?usp=sharing"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
