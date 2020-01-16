import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

list_test = [1,2,3,4,5,6]
CREDENTIALS_FILE = 'key.json'  # имя файла с закрытым ключом

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',
                                                                                  'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

#Create table
spreadsheet = service.spreadsheets().create(body = {
    'properties': {'title': 'InnaTest', 'locale': 'ru_RU'},
    'sheets': [{'properties': {'sheetType': 'GRID',
                               'sheetId': 0,
                               'title': 'InnaTest',
                               'gridProperties': {'rowCount': 8, 'columnCount': 5}}}]
}).execute()
print('Spreadsheet ID: {0}'.format(spreadsheet.get('spreadsheetId')))
#Show and define sheetId
sheetId = spreadsheet.get('spreadsheetId')

#Add access to sheet
driveService = apiclient.discovery.build('drive', 'v3', http = httpAuth)
shareRes = driveService.permissions().create(
    fileId = spreadsheet['spreadsheetId'],
    body = {'type': 'user', 'role': 'writer', 'emailAddress': 'slvjova.inna@gmail.com'},  # доступ на чтение кому угодно
    fields = 'id'
).execute()

#Page is availible on https://docs.google.com/spreadsheets/d/{sheetsID}/edit#gid=0

#Set some value on the table
results = service.spreadsheets().values().batchUpdate(spreadsheetId = spreadsheet['spreadsheetId'], body = {
    "valueInputOption": "USER_ENTERED",
    "data": [
        {"range": "InnaTest!A1:C1",
         "majorDimension": "ROWS",     # сначала заполнять ряды, затем столбцы (т.е. самые внутренние списки в values - это ряды)
         "values": list_test}

        #{"range": "Сие есть название листа!D5:E6",
        # "majorDimension": "COLUMNS",  # сначала заполнять столбцы, затем ряды (т.е. самые внутренние списки в values - это столбцы)
        # "values": [["This is D5", "This is D6"], ["This is E5", "=5+5"]]}
    ]
}).execute()