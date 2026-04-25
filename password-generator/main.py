import random


password_length = int(input("Enter the number of characters in your password: "))
password = ""
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+"

all_chars = lowercase + uppercase + numbers + symbols

for i in range(password_length):
    password += random.choice(all_chars)

print(f"Your password is: {password}")
