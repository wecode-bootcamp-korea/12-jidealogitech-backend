import os 
import django 
import csv 
import sys 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'logitech.settings')
django.setup()

from products.models import Color

CSV_PATH_COLOR = './logitech_color.csv'

with open(CSV_PATH_COLOR) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader: 
        if row[0]:
            color = row[0]
            
            Color.objects.create(
                color       = color,
                )