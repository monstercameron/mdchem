import re

# function to validate email


def validate_email(email):

    print("Validating email -->", email)
    # email patern
    EMAIL_REGEX = re.compile(
        r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$')

    # if the pattern doesnt match then return false, if true return true
    if not EMAIL_REGEX.match(email):
        print(email, "isn't properly formatted!")
        return False
    print(email, "is properly formatted!")
    return True

# validate password with rule:
#   atleast 1 caps, 1 lower, 1 number


def validate_password(password):

    print('Validating password', password)

    # password pattern
    PW_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')

    # if it can't match the pattern return false, but if it can return true
    if not PW_REGEX.match(password):
        print(password, "password isn't properly formatted!")
        return False
    print(password, "password is properly formatted")
    return True
