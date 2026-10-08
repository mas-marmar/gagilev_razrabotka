from celery import Celery
import smtplib
import time
from email.message import EmailMessage
import pyotp 
import qrcode

def create_totp(mail):
    secret = pyotp.random_base32()
    totp = pyotp.TOTP(secret)

    uri = totp.provisioning_uri(
        name= "MyApp",
        issuer_name=mail
    )

    img = qrcode.make(uri)
    img.save("qr_code.png")

    return secret

def send_email(to_email, subject, body):
    my_email = "masamaslakova@gmail.com"
    my_password = "zeto zzoh kfza cemm"

    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = my_email
    msg["To"] = to_email

    with open("qr_code.png", "rb") as f:
        msg.add_attachment(f.read(), maintype="image", subtype="png", filename="qr-code.png")

    try:
        print("отправка письма")
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(my_email, my_password)
            server.send_message(msg)

    except Exception as e:
        print("отправка не удалась {e}")

send_email(
    "patdesathonor6@gmail.com",
    "Маслакова Мария",
    "Qr_code"
)