"""Configuration for GA4 and Google Ads integration"""

from dataclasses import dataclass

@dataclass
class GA4Config:
    PROPERTY_ID: str = '399455767'
    VIEW_ID: str = '399455767'
    MEASUREMENT_ID: str = 'G-Y2W1NQWP0L'
    STREAM_ID: str = '5324010'
    
    # API endpoints
    GA4_API_ENDPOINT: str = 'analyticsdata.googleapis.com'
    
    # Refresh intervals (in seconds)
    METRICS_REFRESH_INTERVAL: int = 300
    CAMPAIGN_SYNC_INTERVAL: int = 900
    DATA_RETENTION_DAYS: int = 30
    CACHE_DURATION: int = 300

@dataclass
class GoogleAdsConfig:
    CUSTOMER_ID: str = '8437927403'
    DEVELOPER_TOKEN: str = 'HpV1ZGZOKj6JewVzrOdXXw'
    LOGIN_CUSTOMER_ID: str = '8437927403'
    API_VERSION: str = 'v14'
    LINKED_ACCOUNTS: list = ('8437927403',)

@dataclass
class OAuthConfig:
    SCOPES: list = (
        'https://www.googleapis.com/auth/analytics.readonly',
        'https://www.googleapis.com/auth/analytics.manage.users.readonly',
        'https://www.googleapis.com/auth/analytics',
        'https://www.googleapis.com/auth/adwords',
        'https://www.googleapis.com/auth/analytics.edit',
        'https://www.googleapis.com/auth/analytics.provision'
    )
    
    CLIENT_ID: str = '22083613754-d1omeg2958vrsndpqg2v1jp0ncm7sr23.apps.googleusercontent.com'
    CLIENT_SECRET: str = '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'
    REDIRECT_URIS: list = (
        'https://allervie.bluehighlightedtext.com/oauth2callback',
        'https://allervie.bluehighlightedtext.com/auth/callback'
    )