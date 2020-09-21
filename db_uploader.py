import os 
import django 
import csv 
import sys 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'logitech.settings')
django.setup()

from products.models import Main_category, Category

CSV_PATH_MAIN = './Main_category.csv'

with open(CSV_PATH_MAIN) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader: 
        if row[0]:
            main_category_name = row[0]
        category_name = row[1]
        main_category_id = Main_category.objects.get(name = main_category_name).id
        
        #Category.objects.create(name = category_name, main_category_id = main_category_id)
        # category_id = Category.ob 