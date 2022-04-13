# GOOGLE API for CODE

from google.oauth2 import service_account

from googleapiclient.discovery import build



from google.oauth2 import service_account


SERVICE_ACCOUNT_FILE = 'key.json'

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds=None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1NFpUsiy9eGmI-qPEMqHgHAyIKFQVW_trVB7i15x2IvQ'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                        range="Cohorts!A1:H13").execute()
values = result.get('values', [])

print(values)




