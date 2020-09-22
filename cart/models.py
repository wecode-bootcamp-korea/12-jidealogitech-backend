from django.db import models
from account.models import Account
# from product.models import Product

class Cart(models.Model):
    cart_id            = models.ForeignKey(Account, on_delete = models.CASCADE)
    # product_title      = models.ForeignKEY(Product, on_delete = models.CASCAED)
    image              = models.URLField(max_length=200)
    count              = models.IntegerField(default=0)
    price              = models.IntegerField(default=0)
    delete             = models.CharField(max_length=50)
    
   
    class Meta:
        db_table : 'carts'
