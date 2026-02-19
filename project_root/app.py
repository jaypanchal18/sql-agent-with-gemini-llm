from flask import Flask, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/', methods=['GET'])
def home():
    try:
        return jsonify({"message": "Server is running!"}), 200
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        logging.error(f"Failed to start the server: {e}")