age = 19
if age < 6:
    price = 0
elif age in range(6, 19):
    price = 10
elif age > 60:
    price = 10
else:
    price = 20

print(price)