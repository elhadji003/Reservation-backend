from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils import timezone

def send_reservation_confirmation_email(user, slot, calendar_link):
    context = {
        "user": user,
        "slot": slot,
        "calendar_link": calendar_link,
        "current_year": timezone.now().year,
    }

    subject = "Confirmation de votre réservation"
    html_content = render_to_string("emails/reservation_confirmation.html", context)

    email = EmailMessage(
        subject=subject,
        body=html_content,
        from_email="no-reply@tondomaine.com",  # Remplace par ton adresse
        to=[user.email],
    )
    email.content_subtype = "html"
    email.send()
