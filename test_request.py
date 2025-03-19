import requests

url = "http://127.0.0.1:5000/add_property"
new_property = {
    "Property Name": "Sunset Apartments",
    "Property Address": "789 Ocean Drive",
    "City": "Los Angeles",
    "State": "CA",
    "Number of Units": 120,
    "Unit Type": "2 BR / 2 BA",
    "Bedrooms": 2,
    "Bathrooms": 2,
    "Rentable Square Footage": 950,
    "Asking Rent Per Month": 2400
}

response = requests.post(url, json=new_property)
print(response.json())  # Should return {"message": "Property added successfully!"}
