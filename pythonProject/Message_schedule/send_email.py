import smtplib
import ssl
from email.message import EmailMessage

smtp_server = "smtp.ethereal.email"
smtp_port = 587
sender_email = "gerard.will@ethereal.email"
password = "8VAFbry682yuEDVkmq"


class EmailSender:
    def __init__(self, sender_email, password):
        self.sender_email = sender_email
        self.password = password

    def send(self, receiver_email, subject, body):
        em = EmailMessage()
        em['From'] = self.sender_email
        em['To'] = receiver_email
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()
        with smtplib.SMTP(host=smtp_server, port=smtp_port) as smtp:
            smtp.starttls(context=context)
            smtp.login(self.sender_email, self.password)
            smtp.send_message(em)

        print("Email sent successfully")


sender = EmailSender(sender_email=sender_email, password=password)
sender.send(receiver_email="receiver_email@example.com", subject="Hello from python", body="This is a test")
