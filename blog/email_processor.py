from email.message import EmailMessage

import smtplib
from django.conf import settings
from django.contrib import messages


def send_email(req, sub, msg_to, msg_message, msg_from=settings.EMAIL_HOST_USER):
    msg = EmailMessage()

    msg["Subject"] = sub
    msg["From"] = msg_from
    msg["To"] = msg_to
    msg.set_content(msg_message)
    hml = f"""
                <!Doctype html>
                <html>
                <body>
                <h1 style='font-style:italic;'>{sub}</h1>
                <p style='color:SlateGray;'>  {msg_message} </p>
                </body>
                </html>
                </html>
                """
    msg.add_alternative(hml, subtype='html')
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            smtp.send_message(msg)
            messages.success(req, f"News update messages sent successfully.")

    except UserWarning as e:
        messages.info(req, f"Sorry,there seems to be something wrong with internet connection")
