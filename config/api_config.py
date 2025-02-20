"""Configuration for Google APIs and Analytics"""

class APIConfig:
    # GA4 Configuration
    GA4_PROPERTY_ID = '399455767'
    GA_VIEW_ID = '399455767'
    MEASUREMENT_ID = 'G-Y2W1NQWP0L'
    STREAM_ID = '5324010'
    
    # API Endpoints
    GA4_API_ENDPOINT = 'analyticsdata.googleapis.com'
    GOOGLE_ADS_API_VERSION = 'v14'
    
    # Scopes
    SCOPES = [
        'https://www.googleapis.com/auth/analytics.readonly',
        'https://www.googleapis.com/auth/analytics.manage.users.readonly',
        'https://www.googleapis.com/auth/analytics',
        'https://www.googleapis.com/auth/adwords',
        'https://www.googleapis.com/auth/analytics.edit',
        'https://www.googleapis.com/auth/analytics.provision'
    ]
    
    # Sync Configuration
    METRICS_REFRESH_INTERVAL = 300  # 5 minutes
    CAMPAIGN_SYNC_INTERVAL = 900    # 15 minutes
    DATA_RETENTION_DAYS = 30
    CACHE_DURATION = 300