from django.db import models
from account.models import Account
# from product.models import Product

class Cart(models.Model):
    account            = models.ForeignKey(Account, on_delete = models.CASCADE)
    # product           = models.ForeignKEY(Product, on_delete = models.CASCAED)
    count              = models.IntegerField(default=0)
    
    
    class Meta:
        db_table : 'carts'
