# Allervie Analytics OAuth Flow

## Overview
This project provides a comprehensive analytics solution with OAuth2 authentication for accessing Google Analytics data.

## Setup
1. Clone the repository
2. Copy `.env.example` to `.env` and fill in your configuration
3. Copy `client_secret.example.json` to `client_secret.json` and add your OAuth credentials
4. Create a virtual environment: `python -m venv venv`
5. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
6. Install dependencies: `pip install -r requirements.txt`

## Configuration
The application requires several configuration files:

### Environment Variables (.env)
- Google Analytics credentials
- OAuth 2.0 configuration
- Application settings
- API configuration

### OAuth Configuration (client_secret.json)
- Google OAuth 2.0 credentials
- Redirect URIs
- JavaScript origins

## Usage
1. Start the application: `python run.py`
2. Navigate to `http://localhost:8080`
3. Follow the OAuth flow to authenticate
4. Access analytics data through the web interface

## Development
- Run tests: `pytest`
- Check code style: `flake8`
- Format code: `black .`

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Security Notes
- Never commit sensitive credentials
- Use environment variables for secrets
- Keep OAuth tokens secure
- Regularly rotate credentials

## License
MIT