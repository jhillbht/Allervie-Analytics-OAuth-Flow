import pytest
import os
from dotenv import load_dotenv

@pytest.fixture(autouse=True)
def load_env():
    load_dotenv()
    
@pytest.fixture
def app_config():
    return {
        'GA4_PROPERTY_ID': os.getenv('GA4_PROPERTY_ID'),
        'FLASK_SECRET_KEY': os.getenv('FLASK_SECRET_KEY')
    }