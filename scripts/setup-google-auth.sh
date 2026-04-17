#!/bin/bash
# Restore Gemini CLI OAuth credentials from GitHub Secrets.
set -e

mkdir -p ~/.gemini

echo "${GEMINI_TOKEN_JSON}" > ~/.gemini/oauth_creds.json

echo "Gemini OAuth credentials restored."
