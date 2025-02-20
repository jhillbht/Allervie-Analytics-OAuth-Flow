"""Main configuration file for Allervie Analytics"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base configuration
class Config:
    # Basic app config
    DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 8080))
    APP_DOMAIN = os.getenv('APP_DOMAIN', 'allervie.bluehighlightedtext.com')
    
    # File paths
    BASE_DIR = Path(__file__).parent
    CREDENTIALS_PATH = BASE_DIR / 'credentials'
    LOGS_PATH = BASE_DIR / 'logs'
    
    # Create required directories
    CREDENTIALS_PATH.mkdir(exist_ok=True)
    LOGS_PATH.mkdir(exist_ok=True)
    
    # Google Analytics config
    GA4_PROPERTY_ID = os.getenv('GA4_PROPERTY_ID')
    GA_VIEW_ID = os.getenv('GA_VIEW_ID')
    MEASUREMENT_ID = os.getenv('MEASUREMENT_ID')
    STREAM_ID = os.getenv('STREAM_ID')
    
    # Google Ads config
    GOOGLE_ADS_CUSTOMER_ID = os.getenv('GOOGLE_ADS_CUSTOMER_ID')
    GOOGLE_ADS_DEVELOPER_TOKEN = os.getenv('GOOGLE_ADS_DEVELOPER_TOKEN')
    GOOGLE_ADS_LOGIN_CUSTOMER_ID = os.getenv('GOOGLE_ADS_LOGIN_CUSTOMER_ID')
    
    # OAuth config
    GOOGLE_OAUTH_SCOPES = os.getenv('GOOGLE_OAUTH_SCOPES').split(',')
    
    # Data sync config
    METRICS_REFRESH_INTERVAL = int(os.getenv('METRICS_REFRESH_INTERVAL', 300))
    CAMPAIGN_SYNC_INTERVAL = int(os.getenv('CAMPAIGN_SYNC_INTERVAL', 900))
    DATA_RETENTION_DAYS = int(os.getenv('DATA_RETENTION_DAYS', 30))
    CACHE_DURATION = int(os.getenv('CACHE_DURATION', 300))
    
    # Service account path
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

# Select configuration based on environment
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

def get_config():
    """Get the appropriate configuration based on environment"""
    env = os.getenv('FLASK_ENV', 'development')
    return config.get(env, config['default'])