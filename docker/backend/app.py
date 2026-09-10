from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/")
def home():
    return jsonify({
        "message": "Backend API is running",
        "status": "success"
    })

@app.route("/api")
def api():
    return jsonify({
        "application": "FA1 Backend",
        "message": "Hello from Flask API"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)