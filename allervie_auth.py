from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
import os

class AllervieAuth:
    def __init__(self):
        self.client_secrets_file = 'client_secret.json'
        self.scopes = [
            'https://www.googleapis.com/auth/analytics.readonly',
            'https://www.googleapis.com/auth/analytics.manage.users.readonly'
        ]

    def create_auth_flow(self, redirect_uri):
        flow = Flow.from_client_secrets_file(
            self.client_secrets_file,
            scopes=self.scopes,
            redirect_uri=redirect_uri
        )
        return flow

    def credentials_to_dict(self, credentials):
        return {
            'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes
        }

    def dict_to_credentials(self, credentials_dict):
        return Credentials(
            **credentials_dict
        )