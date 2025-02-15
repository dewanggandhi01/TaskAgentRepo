import re

input_file = "/c/Project_1_TDS/data/email.txt"
output_file = "/c/Project_1_TDS/data/email-sender.txt"

try:
    # Read email content
    with open(input_file, "r", encoding="utf-8") as f:
        email_content = f.read()

    # Regex to find email addresses
    match = re.search(r"From:\s*([^\s]+@[^\s]+)", email_content)

    if match:
        sender_email = match.group(1)

        # Write extracted email to file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(sender_email)

        print(f"Done! Extracted email saved to {output_file}")
    else:
        print("No sender email found in the email content.")

except Exception as e:
    print(f"Error: {e}")
