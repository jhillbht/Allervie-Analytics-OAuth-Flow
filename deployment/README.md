# Deployment Guide for Allervie Analytics

## DigitalOcean Setup

### Prerequisites
1. Enable required APIs in Google Cloud Console
2. Configure OAuth consent screen
3. Set up service account with appropriate permissions

### Environment Variables
Configure the following in DigitalOcean's environment variables:

1. Basic Configuration
```
FLASK_APP=run.py
FLASK_ENV=production
PORT=8080
HOST=0.0.0.0
DEBUG=false
APP_DOMAIN=allervie.bluehighlightedtext.com
```

2. Google Analytics & Ads Configuration
```
GA4_PROPERTY_ID=399455767
GA_VIEW_ID=399455767
MEASUREMENT_ID=G-Y2W1NQWP0L
STREAM_ID=5324010
```

3. API Configuration
```
GA4_API_ENDPOINT=analyticsdata.googleapis.com
GOOGLE_ADS_API_VERSION=v14
```

### Service Account Setup
1. Mount service account key at `/app/service-account-key.json`
2. Configure necessary permissions
3. Set up API quota monitoring

### OAuth Configuration
1. Add domain to authorized JavaScript origins
2. Configure callback URLs
3. Set up proper CORS settings

### Security Considerations
1. Use Runtime secrets for sensitive values
2. Implement rate limiting
3. Set up proper logging
4. Monitor API quotas