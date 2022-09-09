
#Ask if the user wants to generate password
#If yes ask for password length
#then generate password
#then print password
#if user chooses no exit the program

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$()%,./")
def generate_password():
    password_length = int(input("How long would you like your password to be : "))

    random.shuffle(characters)
    password = []
    
    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Do you want to generate a password (Yes or No) ")
if option.lower() == "Yes".lower():
    generate_password()
elif option.lower() == "No".lower():
    print("Program ended")
else:
    print("Invalid input, please enter Yes or No ")
    