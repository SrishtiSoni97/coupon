from rest_framework import views, status, permissions
from rest_framework.response import Response
from django.utils import timezone
from .models import OTPVerification
from .tasks import send_otp_task
from redemptions.models import UserCoupon
from coupons.models import Coupon

class RequestOTPView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, coupon_id):
        user = request.user
        # Check if already collected
        if UserCoupon.objects.filter(user=user, coupon_id=coupon_id).exists():
            return Response({"error": "Coupon already collected"}, status=status.HTTP_400_BAD_REQUEST)

        # Trigger Celery Task
        send_otp_task.delay(user.id, user.phone_number, coupon_id)
        return Response({"message": "OTP sent successfully via WhatsApp"}, status=status.HTTP_200_OK)

class VerifyOTPView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, coupon_id):
        otp_input = request.data.get('otp')
        user = request.user
        
        try:
            verification = OTPVerification.objects.filter(
                user=user, 
                coupon_id=coupon_id,
                is_verified=False,
                expires_at__gt=timezone.now()
            ).latest('created_at')
        except OTPVerification.DoesNotExist:
            return Response({"error": "Invalid or expired OTP"}, status=status.HTTP_400_BAD_REQUEST)
            
        if verification.otp_code == otp_input:
            verification.is_verified = True
            verification.save()
            
            # Collect Coupon
            coupon = Coupon.objects.get(id=coupon_id)
            UserCoupon.objects.create(user=user, coupon=coupon, status='ACTIVE')
            
            return Response({"message": "Coupon collected successfully!"}, status=status.HTTP_201_CREATED)
        
        return Response({"error": "Incorrect OTP"}, status=status.HTTP_400_BAD_REQUEST)
