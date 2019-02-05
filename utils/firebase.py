import firebase_admin
from firebase_admin import credentials, auth
from classes.student import Student
from config.config import db
import os

# if testing on a local machine
file_path = 'utils/secret/serviceAccountKey.json'
file = os.path.isfile(file_path)

# if testing on a remote machine
remote_file_path = '/var/www/mdchem/mdchem/utils/secret/serviceAccountKey.json'
remote_file = os.path.isfile(remote_file_path)

if file:
    cred = credentials.Certificate(file_path)
else:
    cred = credentials.Certificate(remote_file_path)

firebase_admin.initialize_app(cred)


def delete_user(uid):
    auth.delete_user(uid)


def get_user_data(uid):
    user = auth.get_user(uid)
    print('Successfully fetched user data: {0}'.format(user.uid))
    user_record = {'email': user.email, 'UID': user.uid}
    return user_record


def get_user_data_all():
    users = []
    for user in auth.list_users().iterate_all():
        user_record = {'email': user.email, 'UID': user.uid}
        users.append(user_record)
        print('User: ', user.uid, ',User email:', user.email)
    return users


def new_user_to_database():

    print('Checking Firebase For New User.')

    # get all users stored int he database
    all_students = Student.query.all()

    # firebase user
    for user in auth.list_users().iterate_all():
        add_me = False

        # loops through all the stored students
        for student in all_students:
            add_me = True

            # checks to see if the uid already exists on the local database
            if student.uid == user.uid:
                add_me = False
                # stops looping through list when a match is found for a certan uid
                break

        # if there is no match then add a new student
        if add_me:
            # creating new student with email and uid
            student = Student(user.uid, user.email)
            db.session.add(student)
            db.session.commit()


def delete_all_users():
    for fire_base_user in auth.list_users().iterate_all():
        auth.delete_user(fire_base_user.uid)
