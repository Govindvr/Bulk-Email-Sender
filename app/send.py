from __future__ import print_function
from email import message
from app.send_mail import create_draft,create_message,send_message

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


import csv

def send():
    SCOPES = ['https://www.googleapis.com/auth/gmail.compose']
    rows = []
    with open("uploads\details.csv", 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                rows.append(row)
    print(header)
    print(rows)
    # If modifying these scopes, delete the file token.json.
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'app/credentials.json', SCOPES)
            creds = flow.run_local_server(port=5000)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        # results = service.users().labels().list(userId='me').execute()
        # labels = results.get('labels', [])

        # if not labels:
        #     print('No labels found.')
        #     return
        # print('Labels:')
        # for label in labels:
        #     print(label['name'])
        
        sender="manekshagayathri@gmail.com"
       
        # to="temp200731@cet.ac.in"
        # subject="Test Mail"
        # msg="Hi This is a Test Mail"
        # message=create_message(sender,to,subject,msg)
        
        for r in rows:
            to=r[0]
            subject="Test Mail"
            msg="Hi,{name} . Congratulations on being selected as the best Student of CET,Tvm\n".format(name=r[1])
            msg+="Happy Day :)"
            message=create_message(sender,to,subject,msg)
            send_message(service,'me',message)
        
        # create_draft(service,'me',message)
        # send_message(service,'me',message)
    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')


# if __name__ == '__main__':
#     main()