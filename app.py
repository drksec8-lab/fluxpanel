from flask import Flask, render_template, jsonify, request, abort
import json
import os
from datetime import datetime

app = Flask(__name__)

with open("config.json") as f:
    config = json.load(f)

API_KEY = os.getenv("API_KEY", "")
SECRET  = os.getenv("SECRET", "")


def require_api_key(fn):
    from functools import wraps
    @wraps(fn)
    def wrapper(*args, **kwargs):
        key = request.headers.get("X-API-Key", "")
        if key != API_KEY:
            abort(401)
        return fn(*args, **kwargs)
    return wrapper


@app.route("/")
def index():
    return render_template("index.html", app_name=config.get("app_name", "FluxPanel"))


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/api/v1/metrics", methods=["GET"])
@require_api_key
def get_metrics():
    metrics = {
        "timestamp": datetime.utcnow().isoformat(),
        "cpu_pct": 42.5,
        "mem_pct": 67.1,
        "req_per_sec": 120,
    }
    return jsonify(metrics)


@app.route("/api/v1/metrics", methods=["POST"])
@require_api_key
def post_metric():
    data = request.get_json(force=True)
    if not data:
        return jsonify({"error": "empty body"}), 400
    return jsonify({"status": "ok", "received": data}), 201


@app.route("/api/v1/auth", methods=["POST"])
def auth():
    body = request.get_json(force=True) or {}
    token = body.get("token", "")
    if not token:
        return jsonify({"error": "token required"}), 400
    return jsonify({"status": "authenticated", "expires_in": 3600})


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=5000, debug=debug)
# debug log cleared
