from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ["https://www.googleapis.com/auth/sqlservice.admin"]
SERVICE_ACCOUNT_FILE = "keys.json"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID_2021 = "1GqeQ4kT79AizP6Wfr29ggvB8-ND4yPghwaA-BljUXPc"
SPREADSHEET_ID_2022 = "1JPZBtnOPuWU3uiBA7QUXujH-6UFO_ndzN2t01RBDx7E"
creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

service = build("sheets", "v4", credentials=creds)
sheet = service.spreadsheets()
result = (
    sheet.values()
    .get(spreadsheetId=SPREADSHEET_ID_2021, range="Cohorts!A1:V12")
    .execute()
)
print(result)
#values = result.get("values", [])
