import random

def generate_otp():

    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    login_code = ''
    while len(login_code) < 6:
        new_value = random.choice(numbers)
        login_code += new_value

    return login_code