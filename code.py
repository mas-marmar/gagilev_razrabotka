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

secret = create_totp("masamaslakova@gmail.com")
print(secret)