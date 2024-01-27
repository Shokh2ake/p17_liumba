from celery import shared_task
from django.core.mail import send_mail

from apps.utils import send_email


@shared_task
def task_send_email(subject, msg, recipient_list):
    send_email(subject, msg, recipient_list)
    return 'Yuborildi !'

# 10.10.2.164:8000/send/shokhake6690@gmail.com
