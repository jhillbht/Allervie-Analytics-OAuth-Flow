"""
Flask application entry point for Allervie Analytics
"""

import os
from flask import Flask, render_template, jsonify
from dotenv import load_dotenv
from allervie_analytics import AllervieAnalytics, AnalyticsError

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'default-secret-key')

# Initialize analytics
analytics = None

@app.before_first_request
def initialize_analytics():
    global analytics
    try:
        analytics = AllervieAnalytics()
        analytics.initialize_service()
    except Exception as e:
        print(f"Error initializing analytics: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/active-users')
def get_active_users():
    try:
        if not analytics:
            raise AnalyticsError("Analytics not initialized")
        
        data = analytics.get_active_users(days=30)
        return jsonify({
            'success': True,
            'data': data.to_dict(orient='records')
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/traffic-sources')
def get_traffic_sources():
    try:
        if not analytics:
            raise AnalyticsError("Analytics not initialized")
        
        data = analytics.get_traffic_sources(days=30)
        return jsonify({
            'success': True,
            'data': data.to_dict(orient='records')
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_ENV') == 'development')