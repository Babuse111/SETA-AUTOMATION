from typing import final
from googleapiclient.discovery import build
from google.oauth2 import service_account
from httplib2 import Credentials
import pandas as pd
import gspread
from df2gspread import df2gspread as d2g

SCOPES = ["https://www.googleapis.com/auth/sqlservice.admin"]
SERVICE_ACCOUNT_FILE = "keys.json"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive"]
SPREADSHEET_ID_2021 = "1GqeQ4kT79AizP6Wfr29ggvB8-ND4yPghwaA-BljUXPc"
SPREADSHEET_ID_2022 = "1JPZBtnOPuWU3uiBA7QUXujH-6UFO_ndzN2t01RBDx7E"
creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

service = build("sheets", "v4", credentials=creds)
sheet = service.spreadsheets()
sheets_2021 = (
    sheet.values()
    .get(spreadsheetId=SPREADSHEET_ID_2021, range="Cohorts!A1:V12")
    .execute()
)

sheets_2023 = (
    sheet.values()
    .get(spreadsheetId=SPREADSHEET_ID_2022, range="Cohorts!A1:V12")
    .execute()
)

cohort_2021 = sheets_2021.get("values" )
cohort_2022 = sheets_2021.get("values" )

cohort_2021_df = pd.DataFrame(cohort_2021)
cohort_2022_df = pd.DataFrame(cohort_2022)

final_df = pd.concat([cohort_2021_df,cohort_2022_df], axis=0)

SPREADSHEET_ID_FINAL ='1e3mhDmHdFuQnIbO89yqoF9OsY5fxWWAmcodaw1AlL0I'
WORKSHEET_NAME = "Cohort"

d2g.upload(final_df, SPREADSHEET_ID_FINAL,WORKSHEET_NAME, credentials=creds)

print(final_df.head())