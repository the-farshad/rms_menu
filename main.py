# -*- coding: utf-8 -*-

import firebase_admin
from firebase_admin import credentials, firestore
from file_check import file_abs_path as path


def read_data():
    if (not len(firebase_admin._apps)):
        cred = credentials.Certificate(path() + 'ServiceAccountKey.json')
        default_app = firebase_admin.initialize_app(cerd)
    db = firestore.client()
    collection = db.collection(u'clints').document(u'sport-resturant').collection('categories')
    print(collection.stream())



if __name__ == '__main__':
    read_data()
