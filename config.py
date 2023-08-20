import os

# API KEY
API_KEY = os.environ.get('API_KEY')


# Email Settings
SMPT_HOST = os.environ.get('SMPT_HOST')
SMPT_PORT = os.environ.get('SMPT_PORT')
SMPT_USER = os.environ.get('SMPT_USER')
SMPT_PASSWORD = os.environ.get('SMPT_PASSWORD')

MAIL_RECEIVER = os.environ.get('MAIL_RECEIVER')



# Google Sheets Settings
TARGET_GOOGLE_SHEETS = os.environ.get('TARGET_GOOGLE_SHEETS')
TARGET_GOOGLE_SHEETS_INDEX = os.environ.get('TARGET_GOOGLE_SHEETS_INDEX')
SERVICE_ACCOUNT_FILE = os.environ.get('SERVICE_ACCOUNT_FILE')
