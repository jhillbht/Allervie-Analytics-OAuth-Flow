import pytest
from allervie_analytics import AllervieAnalytics
from datetime import datetime, timedelta

@pytest.fixture
def analytics():
    return AllervieAnalytics()

def test_basic_metrics_structure(analytics):
    data = analytics.get_basic_metrics(days=7)
    assert isinstance(data, list)
    assert len(data) > 0
    
    for item in data:
        assert 'date' in item
        assert 'activeUsers' in item
        assert 'newUsers' in item
        assert 'sessions' in item
        assert 'averageSessionDuration' in item