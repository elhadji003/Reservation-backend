from google.oauth2 import service_account
from googleapiclient.discovery import build
from django.conf import settings

def add_event_to_google_calendar(slot):
    try:
        credentials = service_account.Credentials.from_service_account_file(
            str(settings.GOOGLE_SERVICE_ACCOUNT_FILE),
            scopes=["https://www.googleapis.com/auth/calendar"]
        )

        service = build("calendar", "v3", credentials=credentials)

        event = {
            "summary": slot.title,
            "description": getattr(slot, "description", ""),  # évite l'erreur si pas de champ
            "start": {
                "dateTime": slot.start_time.isoformat(),
                "timeZone": "Africa/Dakar",
            },
            "end": {
                "dateTime": slot.end_time.isoformat(),
                "timeZone": "Africa/Dakar",
            },
        }


        created_event = service.events().insert(
            calendarId=settings.GOOGLE_CALENDAR_ID,
            body=event
        ).execute()

        print("Événement créé :", created_event)  # Ajout du print

        return created_event.get("htmlLink")

    except Exception as e:
        print("Erreur lors de l'ajout à Google Calendar :", e)
        return None
