# Generated by Django 2.2.7 on 2019-11-28 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20191128_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='role',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='usertable',
            name='role',
            field=models.CharField(max_length=250),
        ),
    ]
