from email.message import EmailMessage
import ssl
import smtplib

email_sender = ''

email_password = ''
email_receiver = ''

subject = "CuddlyFussyInteger says HI!"
body = """
I am most definitely not gay and I am sure of it
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)


context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
