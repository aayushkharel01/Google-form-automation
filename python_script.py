import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Load credentials
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet (Use the exact name of your Google Sheet)
spreadsheet = client.open("All responses")  
worksheet = spreadsheet.sheet1  # Access the first sheet

# Fetch all responses
data = worksheet.get_all_records()

# Convert to a Pandas DataFrame
df = pd.DataFrame(data)

#format data in csv
df.columns = df.columns.str.strip().str.title()



# Save locally as CSV
df.to_csv("google_form_responses.csv", index=False)

print("Responses saved successfully!")
