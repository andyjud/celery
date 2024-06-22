from celery import shared_task
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from datetime import datetime
from .models import *

@shared_task(name='email_notification')
def send_email_task(subject, body, emailaddress):        
    email = EmailMessage(subject, body, to=[emailaddress])
    email.send()
    return emailaddress


@shared_task(name='monthly_newsletter')
def send_newsletter():
    subject = "Your Monthly Newsletter"
    
    subscribers = MessageBoard.objects.get(id=1).subscribers.filter(
        profile__newsletter_subscribed=True,
    )
    
    for subscriber in subscribers:
        body = render_to_string('a_messageboard/newsletter.html', {'name': subscriber.profile.name})
        email = EmailMessage( subject, body, to=[subscriber.email] )
        email.content_subtype = "html"
        email.send()
    
    current_month = datetime.now().strftime('%B') 
    subscriber_count = subscribers.count()   
    return f'{current_month} Newsletter to {subscriber_count} subs'
