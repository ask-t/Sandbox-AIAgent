#!/bin/bash
# Restore Google OAuth2 credentials from GitHub Secrets so Gemini CLI can authenticate
# without an interactive browser flow.
set -e

mkdir -p ~/.gemini

cat > ~/.gemini/oauth_creds.json << EOF
{
  "client_id": "${GOOGLE_OAUTH_CLIENT_ID}",
  "client_secret": "${GOOGLE_OAUTH_CLIENT_SECRET}",
  "refresh_token": "${GOOGLE_REFRESH_TOKEN}",
  "type": "authorized_user"
}
EOF

# Point Gemini CLI to the credentials file
mkdir -p ~/.config/gemini
cat > ~/.config/gemini/config.json << EOF
{
  "credentialsFile": "${HOME}/.gemini/oauth_creds.json"
}
EOF

echo "Google OAuth credentials restored."
