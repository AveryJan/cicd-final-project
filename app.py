"""Simple sample Accounts Service API for CI validation."""
from flask import Flask, jsonify

app = Flask(__name__)


@app.get('/health')
def health():
    """Return the API health status."""
    return jsonify({'status': 'ok', 'service': 'accounts-service'})


@app.get('/accounts')
def accounts():
    """Return a sample empty accounts collection."""
    return jsonify({'accounts': []})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
