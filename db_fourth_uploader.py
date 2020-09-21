import os 
import django 
import csv 
import sys 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'logitech.settings')
django.setup()

from products.models import Thumbnail, Product

CSV_PATH_THUMBNAIL = './logitech_thumbnail.csv'

with open(CSV_PATH_THUMBNAIL) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader: 
        if row[0]:
            thumbnail_url = row[0]
            product_title = row[1]
            color         = row[2]  

            product_title = Product.objects.get(product_title = product_title.strip()).id

            Thumbnail.objects.create(
                thumbnail_url     = thumbnail_url.strip(),
                product_title_id  = product_title,
                color_id          = color,
                )