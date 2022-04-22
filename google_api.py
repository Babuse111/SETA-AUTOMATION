from asyncio import Future
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import requests

from google.oauth2 import service_account


SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)



# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '187-I9nfOL08XZz4Na5NoMS2z1oCENQYa6PXS_npBYLE'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="moderation! A1:B4").execute()
values = result.get('values', [])

if not values:
    print('No data found.')
    return

print('Name, Major:')
for row in values:
    # Print columns A and E, which correspond to indices 0 and 4.
    print('%s, %s' % (row[0], row[4]))
except HttpError as err:
print(err)


