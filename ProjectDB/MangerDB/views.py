from django.shortcuts import render
from django.http import HttpResponse
from .serializers import data
from .models import Item
import json

# Create your views here.
def homepage(request):
    homepage_title = 'My homepage'
    items = Item.objects.all()
    json_list = json.loads(data)
    return  render(request,'index.html',{'web_title':homepage_title,'items_lists':json_list})

