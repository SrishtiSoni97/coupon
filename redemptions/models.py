from django.db import models
from django.conf import settings

class UserCoupon(models.Model):
    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('REDEEMED', 'Redeemed'),
        ('EXPIRED', 'Expired'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    coupon = models.ForeignKey('coupons.Coupon', on_delete=models.CASCADE)
    collected_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ACTIVE')
    
    class Meta:
        unique_together = ('user', 'coupon')

    def __str__(self):
        return f"{self.user.username} - {self.coupon.code}"

class CouponRedemption(models.Model):
    user_coupon = models.OneToOneField(UserCoupon, on_delete=models.CASCADE)
    redeemed_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Redemption: {self.user_coupon}"
