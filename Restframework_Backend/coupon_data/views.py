from django.shortcuts import render
from .models import  Coupon
from .serializers import CouponSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status,viewsets
from rest_framework.response import Response
# Create your views here.


class CouponList(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # Get 方法
    def list(self, request, **kwargs):
        coupon = Coupon.objects.all()
        serializer = CouponSerializer(coupon, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def detail(self,request,**kwargs):
        coupon = Coupon.objects.all()