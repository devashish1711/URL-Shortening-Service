from flask import Flask, request, jsonify, abort
from datetime import datetime
from models import init_db, create_url, get_url, update_url, delete_url, get_stats, increment_access
from utils import generate_short_code

app = Flask(__name__)
init_db()

@app.route('/shorten', methods=['POST'])
def shorten():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({"error": "Missing 'url'"}), 400

    short_code = generate_short_code()
    now = datetime.utcnow().isoformat()
    result = create_url(data['url'], short_code, now)
    return jsonify(result), 201

# Add GET, PUT, DELETE, and stats endpoints here...

if __name__ == '__main__':
    app.run(debug=True)

