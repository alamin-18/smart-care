from rest_framework.routers import DefaultRouter
from .views import SpecializationViewSet, DoctorViewSet, DesignationViewSet,AvailableTimeViewSet,ReviewViewSet
from django.urls import path, include
router = DefaultRouter()
router.register(r'specialization', SpecializationViewSet, basename='specialization')
router.register(r'list', DoctorViewSet, basename='doctor')
router.register(r'designation', DesignationViewSet, basename='designation')
router.register(r'available-time', AvailableTimeViewSet, basename='available-time')
router.register(r'review', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
]