from django.db import models
from collections import namedtuple

from django.db import connection

# Create your models here.
class Item(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
    title = models.CharField(max_length=100)
    MyClass = models.CharField(max_length=20)
    content = models.CharField(max_length=200)

class User(models.Model):
    # id = models.CharField(max_length=20)
    LIKES = (
        ('差評','bad'),
        ('中等','normal'),
        ('好','good'),
    )
    like = models.CharField(max_length=1,choices=LIKES)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()

def search_id(**kwargs):
    id = kwargs.get('id')
    if id:
        result = Item.objects.raw('SELECT * FROM mangerdb_item WHERE id = %s', [id])
    else:
        result = Item.objects.raw('SELECT * FROM mangerdb_item')
    return result
