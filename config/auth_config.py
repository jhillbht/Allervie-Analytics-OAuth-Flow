"""Authentication configuration for OAuth and service accounts"""

class AuthConfig:
    # OAuth Configuration
    CLIENT_ID = '22083613754-d1omeg2958vrsndpqg2v1jp0ncm7sr23.apps.googleusercontent.com'
    CLIENT_SECRET = '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'
    
    # Google Ads Configuration
    ADS_CUSTOMER_ID = '8437927403'
    ADS_DEVELOPER_TOKEN = 'HpV1ZGZOKj6JewVzrOdXXw'
    
    # Redirect URIs
    REDIRECT_URIS = [
        'https://allervie.bluehighlightedtext.com/oauth2callback',
        'https://allervie.bluehighlightedtext.com/auth/callback'
    ]
    
    # JavaScript Origins
    ALLOWED_ORIGINS = [
        'https://allervie.bluehighlightedtext.com'
    ]