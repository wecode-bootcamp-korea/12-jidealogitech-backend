from django.db import models
# from order.models import Order 
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
    product_banner       = models.CharField(max_length=1000, null=True)
    product_teaser       = models.CharField(max_length=1000, null=True)
    product_key_feature  = models.CharField(max_length=1000, null=True)
    product_title        = models.CharField(max_length=50)
    product_details      = models.CharField(max_length=50)
    product_price        = models.DecimalField(max_digits=5, decimal_places=2)
    product_note         = models.CharField(max_length=50)
    additional_feature   = models.CharField(max_length=1000, null=True)
    specs_details        = models.CharField(max_length=1000)
    recommended_products = models.CharField(max_length=30, null=True)
    category             = models.ForeignKey(Category, on_delete = models.CASCADE)
    
    class Meta:
        db_table = 'products'


class Thumbnail(models.Model):
    thumbnail_url        = models.CharField(max_length=50, null=True)
    product              = models.ForeignKey(Product, on_delete=models.CASCADE)
    color                = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'thumbnails'

class Color(models.Model):
    color                = models.CharField(max_length=10, null=True)      

    class Meta:
        db_table = 'colors'

