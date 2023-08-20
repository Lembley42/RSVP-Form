from config import TARGET_GOOGLE_SHEETS, TARGET_GOOGLE_SHEETS_INDEX, SERVICE_ACCOUNT_FILE
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def connect_google_sheets() -> gspread.Client:
    print('Connecting to Google Sheets...')
    scope = ['https://www.googleapis.com/auth/spreadsheets']
    credentials = ServiceAccountCredentials.from_json(SERVICE_ACCOUNT_FILE, scope)
    client = gspread.authorize(credentials)
    print('Connected!')
    return client


def add_to_google_sheets(contents):
    gsheets = connect_google_sheets()
    sheet = gsheets.open_by_key(TARGET_GOOGLE_SHEETS).get_worksheet(TARGET_GOOGLE_SHEETS_INDEX)
    sheet.append_row(contents)
    return 'Success'

