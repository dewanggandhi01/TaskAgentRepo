#!/bin/bash

# Define file paths
EMAIL_FILE="/c/Project_1_TDS/data/email.txt"
OUTPUT_FILE="/c/Project_1_TDS/data/email-sender.txt"

# Check if the email file exists
if [ ! -f "$EMAIL_FILE" ]; then
    echo "Error: $EMAIL_FILE not found!"
    exit 1
fi

# Read the email content
EMAIL_CONTENT=$(cat "$EMAIL_FILE")

# Call LLM API (Replace YOUR_OPENAI_API_KEY with actual API Key)
API_KEY="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"
RESPONSE=$(curl -s -X POST "https://api.openai.com/v1/chat/completions" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $API_KEY" \
    -d '{
        "model": "gpt-4",
        "messages": [{"role": "user", "content": "Extract only the sender\'s email address from this email:\n\n'"$EMAIL_CONTENT"'"}]
    }')

# Extract the email using jq
SENDER_EMAIL=$(echo "$RESPONSE" | jq -r '.choices[0].message.content' | grep -oP '[\w\.-]+@[\w\.-]+\.\w+')

# Save the extracted email to output file
echo "$SENDER_EMAIL" > "$OUTPUT_FILE"
echo "✅ Extracted sender email saved to $OUTPUT_FILE"

