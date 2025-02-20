from flask import Flask, render_template, jsonify, request, session
from allervie_auth import AllervieAuth
from allervie_analytics import AllervieAnalytics
import os

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

auth = AllervieAuth()
analytics = AllervieAnalytics()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/auth/status')
def auth_status():
    if 'credentials' not in session:
        return jsonify({
            'authenticated': False,
            'auth_url': '/api/auth/login'
        })
    return jsonify({'authenticated': True})

@app.route('/api/analytics/basic')
def get_basic_metrics():
    try:
        days = request.args.get('days', default=30, type=int)
        data = analytics.get_basic_metrics(days)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 8080)))