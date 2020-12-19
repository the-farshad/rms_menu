import csv
import json
import firebase_admin
from firebase_admin import credentials, firestore
from file_check import file_abs_path as path
from file_check import file_exists_check as exist


def jsonify():
    resturant_name = u'Hama Cafe'
    service_key = 'ServiceAccountKey_HEC.json'
    resturant_name_perfix = resturant_name + '_'
    category_name = resturant_name_perfix + u'Categories_V2'
    filename = 'menu.csv'
    output_filename = 'menu.json'
    output = dict()
    js = dict()

    if (not len(firebase_admin._apps)):
        cred = credentials.Certificate(path() + service_key)
        default_app = firebase_admin.initialize_app(cred, {
            'storageBucket': '<BUCKET_NAME>'
        })
    db = firestore.client()
    ref = db.collection(u'clients').document(
        resturant_name).collection(category_name)

    if exist(filename):
        with open(path() + filename, 'r') as fr:
            csv_file = csv.reader(fr)
            reader = list(csv_file)
            try:
                for row in reader:
                    output[row[0]] = {
                        u'mainCat': row[0],
                        u'mainCatInArabic': row[1],
                        u'mainCatInKurdish': row[2],
                        u'mainCatImage': row[14],
                        u'subCats': [],
                    }
                subCat = ''
                i = 0
                for row in reader:
                    if subCat != row[3]:
                        output[row[0]]['subCats'].insert(i, {
                            u'subCatName': row[3],
                            u'subCatNameInArabic': row[4],
                            u'subCatNameInKurdish': row[5],
                            u'mainCatName': row[0],
                            u'items': [],
                        })
                        i += 1
                        subCat = row[3]
                mainCat = ''
                subCat = ''
                i = -1
                j = 0
                for row in reader:
                    if mainCat != row[0]:
                        i = -1
                        mainCat = row[0]
                    if subCat != row[3]:
                        i += 1
                        j = 0
                        subCat = row[3]
                    output[row[0]]['subCats'][i]['items'].insert(j, {
                        u'itemName': row[6],
                        u'itemNameInArabic': row[7],
                        u'itemNameInKurdish': row[8],
                        u'itemPrice': int(row[9]),
                        u'itemOffPrice': int(row[10]),
                        u'itemMainCategoryInArabic': row[1],
                        u'itemMainCategoryInKurdish': row[2],
                        u'itemSubCategory': row[3],
                        u'itemSubCategoryInArabic': row[4],
                        u'itemSubCategoryInKurdish': row[5],
                        u'itemAvailability': bool(row[11]),
                        u'itemImage': row[12],
                        u'itemImagePlaceholder': row[13]
                    })
                    j += 1
                for doc in output:
                    ref.document(doc).set(output[doc])

                for row in reader:
                    item = f'<li class=\"product\"><div style="background-image: url("{row[13]}");" class=\"foodicon\">{row[6]}</br>{row[7]}</br>{row[8]}</br>{row[9]}</div></li>'
                    if row[3] in js:
                        js[row[3]] = js[row[3]]+item
                    else:
                        js[row[3]] = item

                js = f"var Data = {js}"
                print(js)
                with open(output_filename, 'w') as fw:
                    json.dump(output, fw)

                with open('./static/js/data.js', 'w') as fw:
                    json.dump(js, fw)

            except csv.Error as e:
                sys.exit(f'file {filename}, line {reader.line_num}: {e}')


if __name__ == '__main__':
    jsonify()
