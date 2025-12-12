from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/coupons/', include('coupons.urls')),
    path('api/verification/', include('verification.urls')),
    path('api/redemptions/', include('redemptions.urls')),
]
