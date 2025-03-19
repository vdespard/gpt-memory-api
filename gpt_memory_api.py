from flask import Flask, request, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# 🔹 Google Sheets Authentication
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# 🔹 Open the Google Sheet
SHEET_NAME = "gpt_sheets"  # Make sure this matches your Google Sheet name
sheet = client.open(SHEET_NAME).sheet1


# 📌 Endpoint: Get Property Details
@app.route("/get_property", methods=["GET"])
def get_property():
    """Retrieve property details by name."""
    property_name = request.args.get("name")  # Get property name from query params
    data = sheet.get_all_records()

    for row in data:
        if row["Property Name"].lower() == property_name.lower():
            return jsonify(row)  # Return property data as JSON

    return jsonify({"error": "Property not found"}), 404


# 📌 Endpoint: Add New Property Data
@app.route("/add_property", methods=["POST"])
def add_property():
    """Add a new property to Google Sheets."""
    new_data = request.json  # Expecting JSON data from GPT

    # Convert to list format for Google Sheets
    row = [
        new_data.get("Property Name", ""),
        new_data.get("Property Address", ""),
        new_data.get("City", ""),
        new_data.get("State", ""),
        new_data.get("Number of Units", ""),
        new_data.get("Unit Type", ""),
        new_data.get("Bedrooms", ""),
        new_data.get("Bathrooms", ""),
        new_data.get("Rentable Square Footage", ""),
        new_data.get("Asking Rent Per Month", ""),
    ]

    sheet.append_row(row)  # Add the row to Google Sheets
    return jsonify({"message": "Property added successfully!"})


# ✅ Run the API
if __name__ == "__main__":
    app.run(port=5000, debug=True)
