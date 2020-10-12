# -*- coding: utf-8 -*-
import csv
import firebase_admin
from firebase_admin import credentials, firestore, storage, auth
from file_check import file_abs_path as path
from file_check import file_exists_check as exist


def read_data():

    filename = "menu.csv"
    resturant_name= u'Sport_Cafe'
    resturant_name_perfix = resturant_name + '_'
    category_name = resturant_name_perfix + u'Categories'
    subcategory_name = resturant_name_perfix + u'Subcategories'
    items_name = resturant_name_perfix + u'Items'

    if (not len(firebase_admin._apps)):
        cred = credentials.Certificate(path() + 'ServiceAccountKey.json')
        default_app = firebase_admin.initialize_app(cred, {
            'storageBucket': '<BUCKET_NAME>'
        })
    db = firestore.client()
    collection = db.collection(u'clients').document(resturant_name).collection(category_name)

    if exist(filename):
        with open(path() + filename, 'r') as fr:
            reader = csv.reader(fr)
            try:
                for row in reader:

                    category = collection.document(row[0])
                    category.set({
                        u'mainCat': row[0],
                        u'mainCat0': row[0],
                        u'mainCatInArabic': row[1],
                        u'mainCatInKurdish': row[2],
                        u'mainCatImage': row[14],
                    })

                    subCategory = category.collection(subcategory_name).document(row[3])
                    subCategory.set({
                        u'subCatName':  row[3],
                        u'subCatNameInArabic': row[4],
                        u'subCatNameInKurdish': row[5],
                        u'mainCatName': row[0],
                    })
                    item = subCategory.collection(items_name).document(row[6])
                    item.set({
                        u'itemName': row[6],
                        u'itemNameInArabic': row[7],
                        u'itemNameInKurdish': row[8],
                        u'itemPrice': int(row[9]),
                        u'itemOffPrice': int(row[10]),
                        u'itemMainCategory': row[0],
                        u'itemSubCategory': row[3],
                        u'itemAvailability': bool(row[11]),
                        u'itemImage': row[12] ,
                        u'itemImagePlaceholder': row[13],
                    })

                    print (row)

            except csv.Error as e:
                sys.exit(f'file {filename}, line{reader.line_num}: {e}')


if __name__ == '__main__':
    read_data()
