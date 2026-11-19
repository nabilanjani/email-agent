import json
import pandas as pd

# Membaca mock email
with open("data/mock_emails.json", "r", encoding="utf-8") as file:
    emails = json.load(file)

# Membaca test cases
test_cases = pd.read_csv("data/test_cases.csv")

print("=== MOCK EMAIL DATASET ===")
print(f"Jumlah email: {len(emails)}")

for email in emails:
    print(
        email["email_id"],
        "-",
        email["subject"]
    )

print("\n=== TEST CASES ===")
print(test_cases)

print("\nDataset berhasil dibaca!")