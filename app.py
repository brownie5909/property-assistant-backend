from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from assistant_tools import get_property_insights_and_pdf

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Property Assistant API is running!"

@app.route('/generate-report', methods=['POST'])
def generate_report():
    try:
        data = request.json
        address = data.get("address")
        if not address:
            return jsonify({"error": "Missing 'address' in request."}), 400

        result = get_property_insights_and_pdf(address)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Property Assistant is live!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Render sets PORT environment variable
    app.run(host='0.0.0.0', port=port)
