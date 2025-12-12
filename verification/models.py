from django.db import models
from django.conf import settings
import uuid

class OTPVerification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_verified = models.BooleanField(default=False)
    coupon = models.ForeignKey('coupons.Coupon', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.phone_number} - {self.otp_code}"
