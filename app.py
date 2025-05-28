
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Property Assistant is live!"

@app.route('/generate-report', methods=['POST'])
def generate_report():
    data = request.get_json()
    address = data.get("address", "Unknown address")

    # Dummy PDF logic for placeholder
    dummy_response = {
        "download_link": f"https://example.com/fake-report-for-{address.replace(' ', '_')}.pdf"
    }
    return jsonify(dummy_response)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
