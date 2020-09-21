import os 
import django 
import csv 
import sys 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'logitech.settings')
django.setup()

from products.models import Product

CSV_PATH_PRODUCTS = './logitech_products.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader: 
        if row[0:10]:

            product_banner = row[0]
            product_teaser = row[1]
            product_key_feature  = row[2]
            product_title        = row[3]
            product_details      = row[4]
            product_price        = row[5]
            product_note         = row[6]
            additional_feature   = row[7]
            specs_details        = row[8]
            recommended_products = row[9]
            category             = row[10]
            
            Product.objects.create(
                product_banner       = product_banner.strip(),
                product_teaser       = product_teaser.strip(),
                product_key_feature  = product_key_feature.strip(),
                product_title        = product_title.strip(), 
                product_details      = product_details.strip(), 
                product_price        = product_price.strip(), 
                product_note         = product_note.strip(), 
                additional_feature   = additional_feature.strip(), 
                specs_details        = specs_details.strip(), 
                recommended_products = recommended_products.strip(),
                category_id          = category.strip(),
                )