# Generated by Django 2.2.1 on 2019-05-23 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon_data', '0004_auto_20190523_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='coupon_create_at',
            field=models.DateField(),
        ),
    ]
