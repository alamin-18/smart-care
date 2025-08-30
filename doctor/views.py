from django.shortcuts import render
from rest_framework import viewsets
from .models import Doctor,Designation,AvailableTime,Review,Specialization
from .serializers import DoctorSerializer,SpecializationSerializer,DesignationSerializer,AvailableTimeSerializer,ReviewSerializer
from rest_framework import filters
# Create your views here.

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__first_name', 'user__email', 'specialization__name', 'designation__name']
class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
class AvailableTimeViewSet(viewsets.ModelViewSet):
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer