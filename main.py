import random

def generate_password(length):
    password_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()?"
    password = ""
    for i in range(length):
        password += random.choice(password_characters)
    return password

length = int(input("Bitte die Länge des Passworts eingeben: "))

password = generate_password(length)
print(password)