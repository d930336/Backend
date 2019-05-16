from django.contrib import admin
from django.urls import path,include
from MangerDB.views import homepage
from MangerDB.viewset import DataViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'data',DataViewSet)

urlpatterns = [
    path('' , homepage),
    path('api/',include(router.urls)),
    path("api-auth.",include('rest_framework.urls',namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
