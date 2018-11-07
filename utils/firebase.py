import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("utils/secret/serviceAccountKey.json")
firebase_admin.initialize_app(cred)


def get_user_data(uid):
    user = auth.get_user(uid)
    print('Successfully fetched user data: {0}'.format(user.uid))
    return user


def get_user_data_all():
    users = []
    for user in auth.list_users().iterate_all():
        user_record = {'email':user.email, 'UID': user.uid}
        users.append(user_record)
        print('User: ', user.uid, ',User email:', user.email)
    return users