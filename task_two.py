from schedul import add, send_email

add.delay()

send_email.apply_async(countdown=5)

send_email.apply_async(eta=datetime.now() + timedelta(seconds=10))
