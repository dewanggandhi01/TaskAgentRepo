import json

input_file = "C:\\Project_1_TDS\\data\\contacts.json"
output_file = "C:\\Project_1_TDS\\data\\contacts-sorted.json"

try:
    with open(input_file, "r", encoding="utf-8") as f:
        contacts = json.load(f)

    contacts_sorted = sorted(contacts, key=lambda x: (x["last_name"], x["first_name"]))

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(contacts_sorted, f, indent=2)

    print(f"✅ Done! Sorted contacts saved to {output_file}")

except Exception as e:
    print(f"❌ Error: {e}")
