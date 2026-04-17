#!/bin/bash
# Wrapper to run a Gemini CLI agent with a given instruction file.
# Usage: ./scripts/run-gemini-agent.sh <instruction_file>
set -e

INSTRUCTION_FILE="${1}"

if [ -z "${INSTRUCTION_FILE}" ]; then
  echo "Usage: $0 <instruction_file>" >&2
  exit 1
fi

if [ ! -f "${INSTRUCTION_FILE}" ]; then
  echo "Instruction file not found: ${INSTRUCTION_FILE}" >&2
  exit 1
fi

PROMPT="$(cat "${INSTRUCTION_FILE}")"

gemini --yolo --model gemini-2.0-flash "${PROMPT}"
