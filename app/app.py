from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask on AWS Fargate (ECS)!"

@app.route("/metrics")
def metrics():
    return "app_requests_total{method='GET'} 1"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
