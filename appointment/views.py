from django.shortcuts import render
from rest_framework import viewsets
from .models import Patient
from .serializers import AppointmentSerializer
# Create your views here.
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = AppointmentSerializer