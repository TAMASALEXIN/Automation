from flask import Flask, request, redirect, jsonify 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import string
import random
from flask import Flask, render_template
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=False)
    shortcode = db.Column(db.String(6), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_redirect = db.Column(db.DateTime)
    redirect_count = db.Column(db.Integer, default=0)

with app.app_context():
    db.create_all()

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()

    if 'url' not in data:
        return jsonify(error='Url not present'), 400

    shortcode = data.get('shortcode')
    if shortcode:
        if URL.query.filter_by(shortcode=shortcode).first():
            return jsonify(error='Shortcode already in use'), 409
    else:
        shortcode = ''.join(random.choices("_" + string.ascii_uppercase + string.ascii_lowercase + string.digits, k=6))

    new_url = URL(url=data['url'], shortcode=shortcode)
    db.session.add(new_url)
    db.session.commit()

    return jsonify(shortcode=shortcode), 201


@app.route('/<shortcode>', methods=['GET'])
def redirect_to_url(shortcode):
    url = URL.query.filter_by(shortcode=shortcode).first()

    if url is None:
        return jsonify(error='Shortcode not found'), 404

    url.last_redirect = datetime.utcnow()
    url.redirect_count += 1
    db.session.commit()
    return redirect(url.url, code=302)


@app.route('/<shortcode>/stats', methods=['GET'])
def get_stats(shortcode):
    url = URL.query.filter_by(shortcode=shortcode).first()

    if url is None:
        return jsonify(error='Shortcode not found'), 404

    stats = {
        "created": url.created_at.isoformat(),
        "lastRedirect": url.last_redirect.isoformat() if url.last_redirect else None,
        "redirectCount": url.redirect_count
    }

    return jsonify(stats), 200


if __name__ == "__main__":
    os.environ['FLASK_APP'] = 'app.py'
    app.run(host="0.0.0.0", port=8000, debug=True)
