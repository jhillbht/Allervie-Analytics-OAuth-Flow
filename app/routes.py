from flask import render_template, jsonify, request
from app import app
from app.ga_integration import get_analytics_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/analytics')
def analytics():
    try:
        data = get_analytics_data()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500