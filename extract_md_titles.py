import os
import json
import re

docs_dir = "/c/Project_1_TDS/data/docs"  # Update if necessary
output_file = "/c/Project_1_TDS/data/docs/index.json"
index = {}

try:
    # List all Markdown files in /data/docs/
    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)

                # Read the file and extract the first H1 title
                with open(file_path, "r", encoding="utf-8") as f:
                    for line in f:
                        match = re.match(r"^#\s+(.+)", line.strip())  # Match # Heading
                        if match:
                            index[file_path.replace(docs_dir + "/", "")] = match.group(1)
                            break  # Only the first H1

    # Save index.json
    os.makedirs(os.path.dirname(output_file), exist_ok=True)  # Ensure /data/docs/ exists
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)

    print(f"Done! Extracted H1 headings saved to {output_file}")

except Exception as e:
    print(f"Error: {e}")
