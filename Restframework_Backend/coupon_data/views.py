from django.shortcuts import render
from .models import  Coupon,User,judge_duplicate_username,judge_duplicate_userid
from .serializers import CouponSerializer  ,UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status,viewsets,generics
from rest_framework.response import Response


#Creating an endpoint for the root of our API
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


#api root
@api_view(["GET"])
def api_root(request,format=None):
    return Response({
        #reverse 反向解析，目的是找尋url中的name
        'coupons':reverse('coupons',request=request,format=format),
        'users':reverse('users',request=request,format=format)
    })

# Create your views here.
class CouponList(generics.ListAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # Get 方法
    def list(self, request, **kwargs):
        coupon = Coupon.objects.all()
        serializer = CouponSerializer(coupon, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CouponDetail(generics.RetrieveAPIView):
    lookup_field = "coupon_id"
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self,request,**kwargs):
        try:
            user_id =self.get_object().user_id
            user_name = self.get_object().user_name
        except:
            user_id = request.data
            user_name = request.data
        user_id = user_id.get('user_id')
        user_id_duplicate = judge_duplicate_userid(user_id=user_id)

        user_name = user_name.get('user_name')
        user_name__duplicate = judge_duplicate_username(user_name=user_name)


        if user_id_duplicate:
            return Response('ID已被使用', status=status.HTTP_200_OK)
        if user_name__duplicate:
            return Response('名稱已被使用', status=status.HTTP_200_OK)

        #create method
        user_id = request.data.get('user_id')
        user_name = request.data.get('user_name')
        user_gender = request.data.get('user_gender')
        users = User.objects.create(user_id=user_id, user_name=user_name, user_gender=user_gender)
        serializer = UserSerializer(users, context={'request': request})

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserDetail(generics.RetrieveAPIView):
    lookup_field = 'user_id'
    queryset = User.objects.all()
    serializer_class = UserSerializer
