from django.db import models

# Create your models here.
class Item(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
    title = models.CharField(max_length=100)
    MyClass = models.CharField(max_length=20)
    content = models.CharField(max_length=200)


