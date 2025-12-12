from rest_framework import serializers
from .models import UserCoupon
from coupons.serializers import CouponSerializer

class UserCouponSerializer(serializers.ModelSerializer):
    coupon = CouponSerializer(read_only=True)
    class Meta:
        model = UserCoupon
        fields = '__all__'
