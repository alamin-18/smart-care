from rest_framework.routers import DefaultRouter
from .views import PatientViewSet
from django.urls import path, include
router = DefaultRouter()
router.register(r'', PatientViewSet, basename='Patient')
urlpatterns = [
    path('', include(router.urls)),
]