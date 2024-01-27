from django.core.mail import send_mail

from root.settings import EMAIL_HOST_USER


def send_email(subject, msg, to_email: list):
    send_mail("Theme", "Text", EMAIL_HOST_USER, to_email, False, )
    return {"status": "success", "message": f"{', '.join(to_email)} send pochta !"}
