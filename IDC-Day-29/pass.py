###password genrator with while loop to keep asking input values until right value is entered

import random
import string

def password1(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length)) 
    return result_str

def password2(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length)) 
    return result_str
    
    
def password3(length):
    letters = string.digits
    result_str = ''.join(random.choice(letters) for i in range(length)) 
    return result_str

def password4(length):
    letters = string.hexdigits
    result_str = ''.join(random.choice(letters) for i in range(length)) 
    return result_str

while True:
    try:
        length = int(input("Enter password length (8-16): "))
        if length < 8 or length > 16:
            raise ValueError("Password length should be between 8 and 16.")
        else:
            break
    except ValueError as e:
        print("Error:", e)
        continue
        
while True:
    try:
        password_type = int(input("Enter password type (1: lowercase, 2: both case, 3: digits, 4: all mixed): "))
        if password_type < 1 or password_type > 4:
            raise ValueError("Password type should be between 1 and 4.")
        else:
            break
    except ValueError as e:
        print("Error:", e)
        continue

if password_type == 1:
    password = password1(length)
elif password_type == 2:
    password = password2(length)
elif password_type == 3:
    password = password3(length)
else:
    password = password4(length)
    
print("Generated password:", password)