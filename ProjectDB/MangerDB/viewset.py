from .models import Item
from .serializers import UserSerializer

#rest_framework
from rest_framework import  viewsets , status
from rest_framework.decorators import permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class DataViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = UserSerializer
    #設定解析類型
    parser_classes = (JSONParser,)

    def get_permissions(self):
        if self.action in ('create',):
            self.permission_classes = [IsAuthenticated,]
        return [permission() for permission in self.permission_classes]

    #Get 方法
    def list(self, request, **kwargs):
        users = Item.objects.all()
        serializer = UserSerializer(users,context = {'request':request},many=True)

        return Response(serializer.data,status = status.HTTP_200_OK)

    #繼承permission，讓他只在有登入下作業
    @permission_classes((IsAuthenticated,))
    def create(self, request, **kwargs):
        id = request.data.get('id')
        users = Item.objects.create(id = id)
        serializer = UserSerializer(users,context = {'request':request})

        return Response(serializer.data,status=status.HTTP_201_CREATED)
