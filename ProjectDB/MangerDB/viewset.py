from .models import Item
from rest_framework import  viewsets
from .serializers import UserSerializer

class DataViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = UserSerializer