from rest_framework.routers import DefaultRouter
from .views import ContactUsViewSet
from django.urls import path, include
router = DefaultRouter()
router.register(r'', ContactUsViewSet, basename='ContactUs')
urlpatterns = [
    path('', include(router.urls)),
]