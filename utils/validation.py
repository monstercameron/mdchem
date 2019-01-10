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


def validate_password_old(password):

    print('Validating password', password)

    # password pattern
    PW_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')

    # if it can't match the pattern return false, but if it can return true
    if not PW_REGEX.match(password):
        print(password, "password isn't properly formatted!")
        return False
    print(password, "password is properly formatted")
    return True


def validate_password(password):

    # this regex searches for atleast one lower case alphabet
    lowcase = re.compile(r'[a-z]')
    # this regex searches for atleast one upper case alphabet
    upcase = re.compile(r'[A-Z]')
    # this regex searches for atleast one digit
    digit = re.compile(r'(\d)')
    # this regex searches for the special chars
    spec_char = re.compile(f'[!@#]')
    # this regex searches for expressions without any space and atleast 8 characters
    space_8 = re.compile(r'^[a-zA-Z0-9!@#]{8,}$')

    if lowcase.search(password) == None:
        print('The entered password doesn\'t have a lower case character')
    if upcase.search(password) == None:
        print('The entered password doesn\'t have an upper case character')
    if digit.search(password) == None:
        print('The entered password doesn\'t have a digit')
    if spec_char.search(password) == None:
        print('The entered password doesn\'t have a Special characters')
    if space_8.search(password) == None:
        print(
            'The entered password should have atleast 8 characters and no space in between')
    if not spec_char.search(password) is None and not lowcase.search(password) is None and not upcase.search(password) is None and not digit.search(password) is None and not space_8.search(password) is None:
        print('New Password is Valid and Saved')
        return True
    else:
        return False