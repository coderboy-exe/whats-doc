from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet

router = DefaultRouter()
router.register("", UserViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += router.urls