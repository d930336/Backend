# Generated by Django 2.2.1 on 2019-06-25 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_token', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
