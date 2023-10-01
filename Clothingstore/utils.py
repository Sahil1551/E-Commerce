from django.core.mail import send_mail
from django.conf import settings

def send_mail_to_client():
    subject = "Welcome to Mancot"
    message = "Hello " + myUser.username + ", \nWelcome To MANCOT \n Thank You for Visiting our website\n We have sent you an email address for conformation"
