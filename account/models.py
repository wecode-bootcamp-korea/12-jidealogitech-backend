from django.db import models


class Account(models.Model):
    name           =   models.CharField(max_length=50)
    email          =   models.EmailField(max_length=50)
    password       =   models.CharField(max_length=20)
    language       =   models.CharField(max_length=50, null=True)
    country        =   models.CharField(max_length=50, null=True)
    birthday       =   models.IntegerField(default=0,null=True)
    phone          =   models.IntegerField(default=0)
    create_at      =   models.DateTimeField(auto_now_add=True,null=True)
    update_at      =   models.DateTimeField(auto_now_add=True,null=True)
   
    class Meta:
        db_table = 'accounts'

class Cart(models.Model):
    #product       =  models.ForeignKey(Account, on_delete=models.CASCADE,null=True)
    #user          =  models.ForeignKey(Account, on_delete=models.CASCADE,null=True)
    count         =  models.CharField(max_length=20,null=True)  

    class Meta:
        db_table = 'carts'
