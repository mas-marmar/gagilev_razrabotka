from consumer import send_email, cost_value

result1 = send_email.delay(42)
result2 = cost_value.delay(10, 5)

print(result1.get())
print(result2.get())