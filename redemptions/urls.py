from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MyCouponsView, RedeemCouponView

router = DefaultRouter()
router.register(r'my-coupons', MyCouponsView, basename='my-coupons')

urlpatterns = [
    path('', include(router.urls)),
    path('redeem/', RedeemCouponView.as_view(), name='redeem_coupon'),
]
