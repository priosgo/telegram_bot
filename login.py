import gspread
from oauth2client.service_account import ServiceAccountCredentials

def login(file_name):
    print('Starting autentication of google drive...')
    try:
        scope = ['https://www.googleapis.com/auth/drive','https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('SalesDataAnalisis.json', scope)
        print('Getting autorization...')
        client = gspread.authorize(credentials)
        client = client.open(file_name)
        print('connection succesfully...')
        print('')
        return client
    except:
        print('Unable to start credentials')