from config import TARGET_GOOGLE_SHEETS, TARGET_GOOGLE_SHEETS_INDEX, SERVICE_ACCOUNT_FILE
import gspread, json
from oauth2client.service_account import ServiceAccountCredentials

def connect_google_sheets() -> gspread.Client:
    print('Connecting to Google Sheets...')
    scope = ['https://www.googleapis.com/auth/spreadsheets']

    with open(SERVICE_ACCOUNT_FILE, 'r') as f:
        keyfile_dict = json.load(f)

    credentials = ServiceAccountCredentials.from_json_keyfile_dict(keyfile_dict, scope)
    client = gspread.authorize(credentials)
    print('Connected!')
    return client


def add_to_google_sheets(gsheets, contents):
    sheet = gsheets.open_by_key(TARGET_GOOGLE_SHEETS).get_worksheet(TARGET_GOOGLE_SHEETS_INDEX)
    sheet.append_row(contents)
    return 'Success'

