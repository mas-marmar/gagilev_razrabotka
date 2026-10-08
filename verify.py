import pyotp

def verify(secret, user_code):
    totp = pyotp.TOTP(secret)
    result = totp.verify(user_code)
    return result

secret = "7YVR3CESMKO7CYP74IHW7OAZ6R3IRBGJ"

user_code = input()
if verify(secret, user_code):
    print("код верный")
else:
    print("nuh uh")