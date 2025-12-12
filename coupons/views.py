from rest_framework import viewsets, permissions
from .models import Coupon
from .serializers import CouponSerializer

class CouponViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Publicly list active coupons.
    """
    queryset = Coupon.objects.filter(is_active=True)
    serializer_class = CouponSerializer
    permission_classes = [permissions.AllowAny]
