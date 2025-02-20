from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest
from datetime import datetime, timedelta
import os

class AllervieAnalytics:
    def __init__(self):
        self.client = BetaAnalyticsDataClient()
        self.property_id = os.getenv('GA4_PROPERTY_ID')

    def get_basic_metrics(self, days=30):
        start_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
        end_date = datetime.now().strftime('%Y-%m-%d')

        request = RunReportRequest(
            property=f'properties/{self.property_id}',
            dimensions=[{'name': 'date'}],
            metrics=[
                {'name': 'activeUsers'},
                {'name': 'newUsers'},
                {'name': 'sessions'},
                {'name': 'averageSessionDuration'}
            ],
            date_ranges=[{
                'start_date': start_date,
                'end_date': end_date
            }]
        )

        response = self.client.run_report(request)
        return self._format_response(response)

    def _format_response(self, response):
        data = []
        for row in response.rows:
            data_point = {
                'date': row.dimension_values[0].value
            }
            for i, metric in enumerate(response.metric_headers):
                data_point[metric.name] = float(row.metric_values[i].value)
            data.append(data_point)
        return data