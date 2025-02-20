from google.oauth2 import service_account
from google.analytics.data_v1beta import BetaAnalyticsDataClient
import os

def get_analytics_client():
    credentials = service_account.Credentials.from_service_account_file(
        'service-account-key.json',
        scopes=['https://www.googleapis.com/auth/analytics.readonly']
    )
    return BetaAnalyticsDataClient(credentials=credentials)

def verify_auth():
    try:
        client = get_analytics_client()
        property_id = os.getenv('GA4_PROPERTY_ID')
        return {
            'status': 'success',
            'message': 'Successfully authenticated with GA4',
            'property_id': property_id
        }
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }