from django.contrib import admin
from django.urls import path,include
from coupon_data import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'coupons', CouponList)


# urlpatterns = [
#     path('',views.api_root,name = 'coupons'),
#     path('api',views.api_root,name='users'),
#     path('api/coupons/', views.CouponList.as_view()),
#     path('api/coupons/<coupon_id>/',views.CouponDetail.as_view()),
#     path('api/users/',views.UserList.as_view()),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     # path('admin/', admin.site.urls),
# ]

urlpatterns = [
    path('',views.api_root),
    path('api/coupons/', views.CouponList.as_view(),name = 'coupons'),
    path('api/coupons/<coupon_id>/',views.CouponDetail.as_view(),name = 'coupon-detail'),
    path('api/users/',views.UserList.as_view(),name = 'users'),
    path('api/users/<user_id>/',views.UserDetail.as_view(),name='user-detail'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('admin/', admin.site.urls),
]