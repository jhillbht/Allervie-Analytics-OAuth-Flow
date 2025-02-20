import pytest
from allervie_auth import AllervieAuth
from google.oauth2.credentials import Credentials

@pytest.fixture
def auth():
    return AllervieAuth()

def test_credentials_conversion(auth):
    test_creds = {
        'token': 'test_token',
        'refresh_token': 'test_refresh_token',
        'token_uri': 'https://oauth2.googleapis.com/token',
        'client_id': 'test_client_id',
        'client_secret': 'test_client_secret',
        'scopes': ['https://www.googleapis.com/auth/analytics.readonly']
    }
    
    credentials = auth.dict_to_credentials(test_creds)
    assert isinstance(credentials, Credentials)
    
    converted_dict = auth.credentials_to_dict(credentials)
    assert converted_dict == test_creds