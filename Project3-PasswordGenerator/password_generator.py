import random
import string

while True:
    print("\n===== PASSWORD GENERATOR =====")

    length = int(input("Enter password length: "))

    characters = string.ascii_letters + string.digits

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)

    choice = input("Generate another password? (y/n): ")

    if choice.lower() != "y":
        print("Program Closed.")
        break