from rest_framework import viewsets, permissions, status, views
from rest_framework.response import Response
from .models import UserCoupon, CouponRedemption
from .serializers import UserCouponSerializer

class MyCouponsView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserCouponSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserCoupon.objects.filter(user=self.request.user)

class RedeemCouponView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        coupon_code = request.data.get('coupon_code')
        try:
            user_coupon = UserCoupon.objects.get(
                user=request.request.user, 
                coupon__code=coupon_code, 
                status='ACTIVE'
            )
            user_coupon.status = 'REDEEMED'
            user_coupon.save()
            
            CouponRedemption.objects.create(user_coupon=user_coupon)
            
            return Response({"message": "Coupon redeemed successfully!"}, status=status.HTTP_200_OK)
        except UserCoupon.DoesNotExist:
            return Response({"error": "Invalid or already redeemed coupon."}, status=status.HTTP_400_BAD_REQUEST)
