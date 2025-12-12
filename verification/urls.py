from django.urls import path
from .views import RequestOTPView, VerifyOTPView

urlpatterns = [
    path('request/<int:coupon_id>/', RequestOTPView.as_view(), name='request_otp'),
    path('verify/<int:coupon_id>/', VerifyOTPView.as_view(), name='verify_otp'),
]
