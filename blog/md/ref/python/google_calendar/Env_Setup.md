Create a Python command-line application that makes requests to the Google Calendar API.

Pre-requisites:
1- Python 3.10.7 or greater
2- download pip, write this command in python : pip install pip
3- Create a Google cloud project:
- In the [Google Cloud console](https://console.cloud.google.com/projectcreate), go to Menu menu > IAM & Admin > Create a Project.
- Enter project Name
- Click create 

4- Enable your google calendar 

Set up Environment:

1- enable API
- In the [Google Cloud console](https://console.cloud.google.com/projectcreate), click on Enable to enable API

2- Configure the OAuth consent screen
- In the [Google Cloud console](https://console.cloud.google.com/projectcreate) go to Menu menu > APIs & Services > OAuth consent screen.
- For User type select Internal, then click Create.
- Complete the app registration form, then click Save and Continue.
- For now, you can skip adding scopes and click Save and Continue. In the future, when you create an app for use outside of your Google Workspace organization, you must change the User type to External, and then, add the authorization scopes that your app requires.
- Review your app registration summary. To make changes, click Edit. If the app registration looks OK, click Back to Dashboard.

3- Authorize credentials for a desktop application
- In the [Google Cloud console](https://console.cloud.google.com/projectcreate), go to Menu menu > APIs & Services > Credentials
- Click Create Credentials > OAuth client ID.
- Click Application type > Desktop app.
- In the Name field, type a name for the credential. This name is only shown in the Google Cloud console.
- Click Create. The OAuth client created screen appears, showing your new Client ID and Client secret.
- Click OK. The newly created credential appears under OAuth 2.0 Client IDs.
- Save the downloaded JSON file as credentials.json, and move the file to your working directory.

4- Install the Google client library

use this command: pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

5- Configure the sample
- create a file named quickstart.py
- include this code:

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


def main():
"""Shows basic usage of the Google Calendar API.
Prints the start and name of the next 10 events on the user's calendar.
"""
creds = None

if os.path.exists("token.json"):
creds = Credentials.from_authorized_user_file("token.json", SCOPES)
if not creds or not creds.valid:
if creds and creds.expired and creds.refresh_token:
creds.refresh(Request())
else:
flow = InstalledAppFlow.from_client_secrets_file(
"credentials.json", SCOPES
)
creds = flow.run_local_server(port=0)
with open("token.json", "w") as token:
token.write(creds.to_json())

try:
service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
    print("Getting the upcoming 10 events")
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
      print("No upcoming events found.")
      return

    # Prints the start and name of the next 10 events
    for event in events:
      start = event["start"].get("dateTime", event["start"].get("date"))
      print(start, event["summary"])

except HttpError as error:
print(f"An error occurred: {error}")


if __name__ == "__main__":
main()

6- Run the sample

write this command: python3 quickstart.py

The first time you run the sample, it prompts you to authorize access:

- If you're not already signed in to your Google Account, sign in when prompted. If you're signed in to multiple accounts, select one account to use for authorization.
- Click Accept.
- Your Python application runs and calls the Google Calendar API.

![Screen Shot 2024-10-29 at 3.50.34 PM.png](Screen%20Shot%202024-10-29%20at%203.50.34%20PM.png)

Authorization information is stored in the file system, so the next time you run the sample code, you aren't prompted for authorization.




