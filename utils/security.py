import hashlib
import uuid

# hashes password with randon generate salt
def hash_password(password):
    # generate random salt
    salt = uuid.uuid4().hex
    # return password and salt hash and hash at the end
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest() + '.' + salt

# hashes password with spedified salt
def hash_password_with_salt(password, salt):
    # return password and salt hash and hash at the end
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest() + '.' + salt

def generate_salt():
    # generate randon salt
    return uuid.uuid4().hex

def verify_password(stored_password, user_password):
    # list that stores the password hash and the salt
    salt = stored_password.split('.')

    # checks the hash stored against a hash of the user input
    if salt[0] in hashlib.sha512((user_password + salt[1]).encode('utf-8')).hexdigest():
        return True
    return False
