import re
import time

def min_max_characters(password):
    min_char = 8
    max_char = 20
    n = len(password)
    if n >= min_char and max_char >= n:
        return True
    elif n > max_char:
        print("Only 20 character maximum")
    else:
        print("Minimum of 8 characters")
    return False
        
def one_uppercase_letter(password):
    b = any([l.isupper() for l in password])
    if b == True:
        return True
    else:
        print("At least one Uppercase letter.")
        return False

def one_digit(password):
    b = any([l.isdigit() for l in password])
    if b == True:
        return True
    else:
        print("At least one d1git.")
        return False

def one_character(password):
    special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if(special_char.search(password) != None):
        return True
    else:
        print("At least one speci@l character")
        return False

def check_password(password_here):
    data = [min_max_characters(password_here), 
            one_uppercase_letter(password_here),
            one_digit(password_here), 
            one_character(password_here)]
    return all(data)

def animate_text(t):
    # For visual only, doesn't work in console
    for letter in t:
        print(letter, end='')
        time.sleep(0.1)
    time.sleep(1); print()

print("--Password Checker--".center(50))
note = "No personal information is stored."
animate_text(note)
while True:
    user_password = input("\nType in password: ")
    if user_password == '':
        print("!! Inputted Data should not be empty")
        continue
    b = check_password(user_password)
    if b == True:
        print("Your password is secured! Thank you for letting us know it.")
