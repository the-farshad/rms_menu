import csv
import json
from file_check import file_abs_path as path
from file_check import file_exists_check as exist


def jsonify():
    filename = 'menu.csv'
    output_filename = 'menu.json'
    output = dict()
    js = dict()

    if exist(filename):
        with open(path() + filename, 'r') as fr:
            csv_file = csv.reader(fr)
            reader = list(csv_file)
            try:
                for row in reader:
                    output[row[0]]= {
                        u'mainCat': row[0],
                        u'mainCatInArabic': row[1],
                        u'mainCatInKurdish': row[2],
                        u'mainCatImage': row[14],
                        u'subcategories':{},
                        }
                for row in reader:
                    output[row[0]]['subcategories'][row[3]]={
                        u'subCatName': row[3],
                        u'subCatNameInArabic': row[4],
                        u'subCatNameInKurdish': row[5],
                        u'mainCatName': row[0],
                        u'items':{},
                    }
                for row in reader:
                    output[row[0]]['subcategories'][row[3]]['items'][row[6]]={
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
                    }

                for row in reader:
                    item = f'<li class=\"product\"><div class=\"foodicon\">{row[6]}</div></li>'
                    if row[3] in js:
                        js[row[3]]=js[row[3]]+item
                    else:
                        js[row[3]]=item

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
