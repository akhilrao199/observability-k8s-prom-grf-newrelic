from flask import Flask, request, render_template, Response
import socket
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint'])

@app.route('/')
def index():
    REQUEST_COUNT.labels(method=request.method, endpoint='/').inc()
    hostname = socket.gethostname()
    return render_template("index.html", pod_name=hostname)

@app.route('/health')
def health():
    return "OK", 200

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
