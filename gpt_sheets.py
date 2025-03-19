import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Authenticate using credentials.json
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet by name
sheet = client.open("gpt_sheets").sheet1  # Change this to your sheet name

# Fetch all records from the sheet
data = sheet.get_all_records()

# Print the data
print("Google Sheet Data:")
for row in data:
    print(row)


