# Google Calender #

One of the uses of google calender is that it allows you to create a plan as an event.
You can also share the plan with your friends and it will remind them to get prepared. 

Google also integrated other products with calendar so Google Maps would direct you to the location automatically. 

In order to successfully create events, you need to:

- Set your OAuth scope to https://www.googleapis.com/auth/calendar so that you have edit access to the user's calendar.
- Ensure the authenticated user has write access to the calendar with the calendarId you provided (for example by calling calendarList.get() for the calendarId and checking the accessRole).

**How to create and share a calendar event?**

example:
_event = service.events().insert(calendarId='primary', body=event).execute()_

in python, call the method _events.insert()_, with these parameters:

- _calendarId_ (string) $is the calendar identifier and can either be the email address of the calendar on which to create the event or a special keyword '_primary_' which will use the primary calendar of the logged in user. If you don't know the email address of the calendar you would like to use, you can check it either in the calendar's settings of the Google Calendar web UI (in the section "Calendar Address") or you can look for it in the result of the calendarList.list() call.
- Optional query parameters:
![optional query parameters.png](optional%20query%20parameters.png)

- _event_ is the event to create with all the necessary details such as start and end. The only two required fields are the _start_ and _end_ times. timed events need to be specified using the _start.dateTime_ and _end.dateTime_ fields. For all-day events, use _start.date_ and _end.date_ instead

Other potential parameters to use are: 

location: Adding an address into the location field enables features such as "time to leave" or displaying a map with the directions.

Event ID: When creating an event, you can choose to generate your own event ID, This enables you to keep entities in your local database in sync with events in Google Calendar.

Attendees: The event you create appears on all the primary Google Calendars of the attendees you included with the same event ID

See the event [reference](https://developers.google.com/calendar/api/v3/reference/events/insert#request-body) for the full set of event fields.
If you choose not to add metadata during creation, you can update many fields using the _events.update()_

- Example: 


event = {
'summary': 'Google I/O 2015',
'location': '800 Howard St., San Francisco, CA 94103',
'description': 'A chance to hear more about Google\'s developer products.',
'start': {
'dateTime': '2015-05-28T09:00:00-07:00',
'timeZone': 'America/Los_Angeles',
},
'end': {
'dateTime': '2015-05-28T17:00:00-07:00',
'timeZone': 'America/Los_Angeles',
},
'recurrence': [
'RRULE:FREQ=DAILY;COUNT=2'
],
'attendees': [
{'email': 'lpage@example.com'},
{'email': 'sbrin@example.com'},
],
'reminders': {
'useDefault': False,
'overrides': [
{'method': 'email', 'minutes': 24 * 60},
{'method': 'popup', 'minutes': 10},
],
},
}

event = service.events().insert(calendarId='primary', body=event).execute()
print 'Event created: %s' % (event.get('htmlLink'))

- Add Attachments to the event

You can add attachments from Google Driver to the calendar events either when the event is created in event.insert() or later as an update with events.patch().

The two parts of attaching a Google Drive file to an event are:

- Get the file alternateLink URL, title, and mimeType from the Drive API Files resource, typically with the files.get() method.
- Create or update an event with the attachments fields set in the request body and the supportsAttachments parameter set to true.

Example:

def add_attachment(calendarService, driveService, calendarId, eventId, fileId):
file = driveService.files().get(fileId=fileId).execute()
event = calendarService.events().get(calendarId=calendarId,
eventId=eventId).execute()

    attachments = event.get('attachments', [])
    attachments.append({
        'fileUrl': file['alternateLink'],
        'mimeType': file['mimeType'],
        'title': file['title']
    })

    changes = {
        'attachments': attachments
    }
    calendarService.events().patch(calendarId=calendarId, eventId=eventId,
                                   body=changes,
                                   supportsAttachments=True).execute()

- Add Video and Phone conferences to events (Hangouts or Google Meet)

To allow creation and modification of conference details, set the conferenceDataVersion request parameter to 1 in the events.insert() method.

There are three types of conferenceData currently supported, as denoted by the conferenceData.conferenceSolution.key.type:

- Hangouts for consumers (eventHangout)
- Classic Hangouts for Google Workspace users (deprecated; eventNamedHangout)
- Google Meet (hangoutsMeet)

You can create a new conference for an event by providing a createRequest with a newly generated requestId which can be a random string. Conferences are created asynchronously, but you can always check the status of your request to let your users know what’s happening.



