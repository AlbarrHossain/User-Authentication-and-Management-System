from django.core.mail import EmailMessage
import os
from django.core.exceptions import ImproperlyConfigured

class Utli:
    @staticmethod
    def send_mail(data):
        try:
            subject = data.get('subject')
            body = data.get('body')
            to_email = data.get('to_email')
            if not subject or not body or not to_email:
                raise ValueError("Missing required email fields.")
            email_from = os.environ.get('EMAIL_FROM')
            if not email_from:
                raise ImproperlyConfigured("EMAIL_FROM environment variable is not set.")
            email = EmailMessage(
                subject=subject,
                body=body,
                from_email=email_from,
                to=[to_email]
            )
            email.send()
            print("Email sent successfully.")
        except Exception as e:
            print(f"Error sending email: {e}")
