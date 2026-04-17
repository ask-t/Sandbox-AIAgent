#!/bin/bash
# Restore Gemini CLI OAuth credentials from GitHub Secrets.
set -e

mkdir -p ~/.gemini
echo "${GEMINI_TOKEN_JSON}" > ~/.gemini/oauth_creds.json

# Write .env so Gemini CLI's sandboxed tools can read credentials via load_dotenv()
cat > .env << EOF
GMAIL_ADDRESS=${GMAIL_ADDRESS}
EOF

echo "Gemini OAuth credentials and .env restored."
