from celery import shared_task
from django.core.mail import EmailMessage

@shared_task
def send_email_task(subject, body, email):        
    email = EmailMessage(subject, body, to=[email])
    email.send()
