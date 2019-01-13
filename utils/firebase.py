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
    for fire_base_user in auth.list_users().iterate_all():

        print('new_user_to_database --> User: ', fire_base_user.uid, ',User email:', fire_base_user.email)
        # print('student --> ' , Student(fire_base_user.uid, fire_base_user.email).__dict__)
        if Student.query.filter_by(uid=fire_base_user.uid).first() is None:
            student = Student(fire_base_user.uid, fire_base_user.email)
            db.session.add(student)
            db.session.commit()


def delete_all_users():
    for fire_base_user in auth.list_users().iterate_all():
        auth.delete_user(fire_base_user.uid)