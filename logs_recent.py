import os
import glob
import sys
sys.stdout.reconfigure(encoding="utf-8")

# Define input directory and output file
input_dir = "/c/Project_1_TDS/data/logs"
output_file = "C:/Project_1_TDS/data/logs-recent.txt"
try:
    # Step 1: Get list of .log files sorted by modification time (most recent first)
    log_files = sorted(glob.glob(os.path.join(input_dir, "*.log")), key=os.path.getmtime, reverse=True)[:10]

    # Step 2: Read the first line from each of these files
    first_lines = []
    for file in log_files:
        with open(file, "r", encoding="utf-8") as f:
            first_line = f.readline().strip()  # Read first line and remove extra spaces
            first_lines.append(first_line)

    # Step 3: Write the first lines into logs-recent.txt
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(first_lines) + "\n")

    print(f"Done! Extracted first lines from 10 most recent logs into {output_file}")

except Exception as e:
    print(f"Error: {e}")