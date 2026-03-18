from flask import Flask, Response  # Added Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST # Added CONTENT_TYPE_LATEST

app = Flask(__name__)

# metric
REQUEST_COUNT = Counter('request_count', 'Total Request Count')

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    return "CI/CD TEST Success"

@app.route('/metrics')
def metrics():
    # This wraps the metrics in a proper response with the correct headers
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
