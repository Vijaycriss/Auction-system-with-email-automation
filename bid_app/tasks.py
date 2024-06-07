from background_task import background
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Product, ParticipantsHistory
from datetime import datetime, timezone

@background(schedule=60)
def send_bid_notification_email(winning_user, product):
    subject = "Congratulations! You participated in the bid"
    message = render_to_string('win_bid_email.html', {'product': product})
    plain_message = strip_tags(message)
    from_email = 'noreply@yourdomain.com'
    to = winning_user.email
    send_mail(subject, plain_message, from_email, [to], html_message=message)
    
@background(schedule=60)
def check_auction_status():
    products = Product.objects.filter(status='live')
    for product in products:
        last_bid = ParticipantsHistory.objects.filter(product=product).order_by('-created').first()
        if last_bid:
            minutes = (datetime.now(timezone.utc) - last_bid.created).seconds / 60
            if minutes >= 3:
                product.winner = last_bid.user
                product.status = 'closed'
                product.save()
                send_bid_notification_email(last_bid.user.email, product.name)
            