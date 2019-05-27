from rest_framework import serializers
from .models import Coupon,User

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ('coupon_id','coupon_class','coupon_content')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id','user_name','user_gender')