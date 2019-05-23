from rest_framework import serializers
from .models import Coupon,User

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ('coupon_id','coupon_title','coupon_class','coupon_content')