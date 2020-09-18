# Generated by Django 3.1.1 on 2020-09-18 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('birthday', models.IntegerField(default=0, null=True)),
                ('phone', models.IntegerField(default=0)),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
    ]