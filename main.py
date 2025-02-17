import string

def validate_password(password):
    if len(password) < 8:
        return "Invalid Password: Password is too short!"
    else:
        has_digit = False
        has_upper = False
        has_regex = False
        for i in password:
            if i.isdigit():
                has_digit = True
            if i.isupper():
                has_upper = True
            if i in string.punctuation:
                has_regex = True
        if has_digit and has_regex and has_upper:
            return "Valid Password"
        else:
            return "Invalid Password: Please make sure to have at least one capital letter, one special character, and one digit."

password = input("Please enter your password: ")
print(validate_password(password))
