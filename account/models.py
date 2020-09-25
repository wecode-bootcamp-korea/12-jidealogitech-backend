from django.db import models

class Account(models.Model):
    email          =   models.EmailField(max_length=50)
    password       =   models.CharField(max_length=100)
    name           =   models.CharField(max_length=50)
    language       =   models.CharField(max_length=50, null=True)
    country        =   models.CharField(max_length=50, null=True)
    birthday       =   models.DateField(null=True)
    phone          =   models.CharField(max_length=20, null=True)
    create_at      =   models.DateTimeField(auto_now_add=True,null=True)
    update_at      =   models.DateTimeField(auto_now_add=True,null=True)
    
    class Meta:
        db_table = 'accounts'