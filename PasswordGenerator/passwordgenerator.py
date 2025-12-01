import random 
import string

def generate_password(length=12):
    characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(characters) for _ in range(length))
    return password

try:
    password_length=int(input("Enter the desired password length: "))
except ValueError:
    print("Invalid input. using default length of 12.")
    password_length=12

password=  generate_password(password_length)
print("Generated Password: ",password)