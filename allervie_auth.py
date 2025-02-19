"""
Allervie Analytics Authentication Module
Handles OAuth 2.0 flow with proper web application credentials
"""

import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from pathlib import Path
import json
import socket

class AllervieAuth:
    def __init__(self):
        # Initialize paths and configurations
        self.base_path = Path(__file__).parent
        self.credentials_path = self.base_path / 'client_secret.json'
        self.token_dir = self.base_path / 'token'
        self.token_path = self.token_dir / 'allervie_token.json'
        
        # GA4 specific configurations - set in .env
        self.property_id = os.getenv('GA4_PROPERTY_ID')
        self.scopes = ['https://www.googleapis.com/auth/analytics.readonly']
        
        # Available ports for OAuth redirect
        self.redirect_ports = [49152, 49153, 49154, 49155]
        
        # Create token directory if it doesn't exist
        self.token_dir.mkdir(exist_ok=True)

    def find_available_port(self):
        """Find the first available port from the configured list"""
        for port in self.redirect_ports:
            try:
                # Try to create a socket with the port
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.bind(('localhost', port))
                sock.close()
                return port
            except socket.error:
                continue
        return None

    def authenticate(self):
        """Handle the complete OAuth 2.0 flow"""
        print("\n=== Allervie Analytics Authentication ===")
        
        if not self.credentials_path.exists():
            print("❌ client_secret.json not found. Please add it to the project root.")
            return None
        
        # Check for existing token
        print("\n1. Checking for existing token...")
        creds = None
        if self.token_path.exists():
            try:
                creds = Credentials.from_authorized_user_file(str(self.token_path), self.scopes)
                print("Found existing token")
            except Exception as e:
                print(f"Error loading existing token: {e}")
        
        # Handle token refresh or new authentication
        if creds and creds.valid:
            print("✅ Existing token is valid")
        else:
            if creds and creds.expired and creds.refresh_token:
                print("Token expired, attempting refresh...")
                try:
                    creds.refresh(Request())
                    print("✅ Token refreshed successfully")
                except Exception as e:
                    print(f"❌ Error refreshing token: {e}")
                    creds = None
            
            if not creds:
                print("\n2. Starting new authentication flow...")
                
                # Find an available port
                port = self.find_available_port()
                if not port:
                    print("❌ No available ports found from the configured list")
                    return None
                
                print(f"Using port {port} for authentication...")
                
                try:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        str(self.credentials_path),
                        self.scopes
                    )
                    
                    creds = flow.run_local_server(
                        port=port,
                        prompt='consent'
                    )
                    
                    # Save the new token
                    with open(self.token_path, 'w') as token:
                        token.write(creds.to_json())
                    print("✅ New token saved successfully")
                
                except Exception as e:
                    print(f"❌ Authentication error: {e}")
                    return None
        
        return creds

    def test_ga4_connection(self, creds):
        """Test the GA4 API connection"""
        print("\n3. Testing GA4 connection...")
        try:
            service = build('analyticsdata', 'v1beta', credentials=creds)
            
            # Make a simple request
            response = service.properties().runReport(
                property=f"properties/{self.property_id}",
                body={
                    "dateRanges": [{"startDate": "yesterday", "endDate": "today"}],
                    "metrics": [{"name": "activeUsers"}]
                }
            ).execute()
            
            users = response['rows'][0]['metricValues'][0]['value']
            print(f"✅ Connection successful! Active users: {users}")
            return True
            
        except Exception as e:
            print(f"❌ Connection error: {e}")
            return False

def main():
    """Main execution flow"""
    auth = AllervieAuth()
    
    # Step 1: Authenticate
    creds = auth.authenticate()
    if not creds:
        print("\n❌ Authentication failed")
        return
    
    # Step 2: Test connection
    if auth.test_ga4_connection(creds):
        print("\n✅ Authentication and connection test completed successfully!")
    else:
        print("\n❌ Connection test failed. Please check the errors above.")

if __name__ == "__main__":
    main()