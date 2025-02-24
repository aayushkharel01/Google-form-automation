readme_content = """\
# 📋 Google Forms Response Fetcher

This Python script automates the process of fetching responses from a Google Form and saving them as a **well-structured CSV file** on your local machine.

## 🚀 Features
- ✅ Automatically retrieves responses from a **linked Google Sheet**.
- ✅ Formats data into a **clean and structured CSV file**.
- ✅ Removes unnecessary spaces and formats dates properly.
- ✅ Supports **UTF-8 encoding** for special characters.

---

## 🛠️ Setup Instructions

### 1️⃣ Prerequisites
Before running the script, ensure you have the following installed:
- **Python (3.7 or higher)**
- **pip (Python package manager)**

---

### 2️⃣ Enable Google API & Obtain Credentials
To allow the script to access your Google Sheet:
1. **Visit Google Cloud Console**: [https://console.cloud.google.com/](https://console.cloud.google.com/)
2. Navigate to **IAM & Admin > Service Accounts**.
3. Create a **new service account** and enable **Google Sheets API**.
4. Under **"Keys"**, select **"Create new key"** and choose **JSON format**.
5. Download the `credentials.json` file and place it in the same directory as the script.

---

### 3️⃣ Share Google Sheet Access
1. Open your **Google Sheet** that is linked to your Google Form.
2. Click **"Share"** in the top-right corner.
3. **Copy the service account email** from `credentials.json` and add it as an **Editor**.
4. Click **"Send"** to grant access.

---

### 4️⃣ Install Required Python Packages
Run the following command to install the necessary dependencies:

```bash pip
 pip install gspread oauth2client pandas
 ▶️ How to Use

    Ensure your credentials.json file is in the script directory.
    Open the script and replace "All responses" with the actual name of your Google Sheet.
    Run the script using:

    python script.py

    The formatted responses will be saved as google_form_responses.csv in the same directory.

📝 Notes & Troubleshooting

    ⚠️ If you encounter authentication errors, ensure your system time is correctly synchronized.
    ⚠️ If the script cannot find your Google Sheet, verify that you've shared access with the correct service account email.
    🛠️ To customize column formatting, modify the pandas DataFrame operations inside the script.
