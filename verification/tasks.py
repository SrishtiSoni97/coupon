from celery import shared_task
from django.utils import timezone
from datetime import timedelta
import random
from .models import OTPVerification
from .services import send_whatsapp_otp
from django.contrib.auth import get_user_model

User = get_user_model()

@shared_task
def send_otp_task(user_id, phone_number, coupon_id=None):
    otp_code = str(random.randint(100000, 999999))
    expires_at = timezone.now() + timedelta(minutes=10)
    
    user = User.objects.get(id=user_id)
    
    OTPVerification.objects.create(
        user=user,
        phone_number=phone_number,
        otp_code=otp_code,
        expires_at=expires_at,
        coupon_id=coupon_id
    )
    
    send_whatsapp_otp(phone_number, otp_code)
    return f"OTP sent to {phone_number}"
