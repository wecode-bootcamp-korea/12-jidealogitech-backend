# Generated by Django 3.1.1 on 2020-09-20 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200920_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='specs_details',
            field=models.TextField(null=True),
        ),
    ]
