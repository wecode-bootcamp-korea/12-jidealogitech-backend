from django.db import models
#from account.models import Account
#from products.models import Product

class Order(models.Model):
    product_title  = models.ManyToManyField("self")
    total_price    = models.IntegerField(default=0)
    order_time     = models.DateTimeField(auto_now_add=True)
    select_count   = models.IntegerField(default=0)
    promotion_code = models.IntegerField(default=0)
    address        = models.CharField(max_length=100)
    status         = models.CharField(max_length=50)
    #account        = models.ForeignKey(Account, on_delete=models.CASCADE)
                   
    class Meta:
        db_table = 'orders'

class Order_product(models.Model):
    order          = models.ForeignKey(Order, on_delete=models.CASCADE)
    #product        = models.ForeignKey(Product, on_delete=models.CASCADE)
    count          = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'order_products'


# Create your models here.
