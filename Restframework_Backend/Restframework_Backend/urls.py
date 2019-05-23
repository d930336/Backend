from django.contrib import admin
from django.urls import path,include
from coupon_data.views import CouponList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'coupons', CouponList)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/coupons/<str:post_id>/',include(router.urls))
    # path('admin/', admin.site.urls),
]
