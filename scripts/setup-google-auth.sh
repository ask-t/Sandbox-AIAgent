#!/bin/bash
# Restore Google OAuth2 credentials from GitHub Secrets so Gemini CLI can authenticate
# without an interactive browser flow.
set -e

# Application Default Credentials (used by GOOGLE_GENAI_USE_GCA=true)
mkdir -p ~/.config/gcloud
cat > ~/.config/gcloud/application_default_credentials.json << EOF
{
  "client_id": "${GOOGLE_OAUTH_CLIENT_ID}",
  "client_secret": "${GOOGLE_OAUTH_CLIENT_SECRET}",
  "refresh_token": "${GOOGLE_REFRESH_TOKEN}",
  "type": "authorized_user"
}
EOF

echo "Google OAuth credentials restored."
