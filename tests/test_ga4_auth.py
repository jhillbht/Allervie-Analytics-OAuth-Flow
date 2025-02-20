import pytest
from ga4_auth import verify_auth

def test_verify_auth():
    result = verify_auth()
    assert 'status' in result
    assert 'message' in result
    
    if result['status'] == 'success':
        assert 'property_id' in result
    else:
        assert isinstance(result['message'], str)