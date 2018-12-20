import firebase_admin
from firebase_admin import credentials, auth
from classes.student import Student
from config.config import db

cred = credentials.Certificate("utils/secret/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

user_list = []


def get_user_data(uid):
    user = auth.get_user(uid)
    print('Successfully fetched user data: {0}'.format(user.uid))
    user_record = {'email':user.email, 'UID': user.uid}
    return user_record


def get_user_data_all():
    users = []
    global user_list
    for user in auth.list_users().iterate_all():
        user_record = {'email':user.email, 'UID': user.uid}
        users.append(user_record)
        user_list.append(user.uid)
        print('User: ', user.uid, ',User email:', user.email)
    return users

def newUserToDatabase():
    for fire_base_user in auth.list_users().iterate_all():

        # print('User: ', fire_base_user.uid, ',User email:', fire_base_user.email)
        # print('student --> ' , Student(fire_base_user.uid, fire_base_user.email).__dict__)
        if Student.query.filter_by(uid=fire_base_user.uid).first() is None:
            student = Student(fire_base_user.uid, fire_base_user.email)
            db.session.add(student)
            db.session.commit()