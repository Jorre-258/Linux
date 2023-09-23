import string
from random import choice

def ask_len():
    while True:
        len = input("Enter the lenght")
        if len.isdigit():
            return len
uppercase = list(string.ascii_uppercase)
lowercase = list(string.ascii_lowercase)
numbers = list(string.digits)
special_characters = list("!@#$%^&*()_+=-{}[]|\:"';<>,.?/~')

len = ask_len()
print(len)
