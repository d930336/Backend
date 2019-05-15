from django.core import  serializers
from .models import Item

data = serializers.serialize("json",Item.objects.all(),fields=('id','title','MyClass','content'))

