import hashlib
import uuid


def hash_password(password):
    # generate random salt
    salt = uuid.uuid4().hex
    # return password and salt hash and hash at the end
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest() + '.' + salt


def verify_password(stored_password, user_password):
    # list that stores the password hash and the salt
    salt = stored_password.split('.')

    # checks the hash stored against a hash of the user input
    if salt[0] in hashlib.sha512((user_password + salt[1]).encode('utf-8')).hexdigest():
        return True
    return False
