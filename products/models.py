from django.db import models
# from account.models import Account

class Main_category(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'main_categories'

class Category(models.Model):
    name = models.CharField(max_length=50)
    main_category = models.ForeignKey(Main_category, on_delete = models.CASCADE)
    
    class Meta:
        db_table = 'categories'

class Product(models.Model):
    product_banner       = models.CharField(max_length=3000, null=True)
    product_teaser       = models.CharField(max_length=3000, null=True)
    product_key_feature  = models.TextField(null=True)
    product_title        = models.CharField(max_length=50)
    product_details      = models.CharField(max_length=100)
    product_price        = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    product_note         = models.CharField(max_length=50, null=True)
    additional_feature   = models.CharField(max_length=3000, null=True)
    specs_details        = models.TextField(null=True)
    recommended_products = models.CharField(max_length=30, null=True)
    category             = models.ForeignKey(Category, on_delete = models.CASCADE)
    color 		         = models.ManyToManyField('Color', through='Thumbnail', through_fields=('product','color'))

    class Meta:
        db_table = 'products'

class Color(models.Model):
    color                = models.CharField(max_length=50, null=True)
    image_url            = models.CharField(max_length=3000,null=True)

    class Meta:
        db_table = 'colors'


class Thumbnail(models.Model):
    thumbnail_url        = models.CharField(max_length=500, null=True)
    product              = models.ForeignKey(Product, on_delete=models.CASCADE)
    color                = models.ForeignKey(Color, on_delete=models.CASCADE, null=True)
    
    class Meta:
        db_table = 'thumbnails'
