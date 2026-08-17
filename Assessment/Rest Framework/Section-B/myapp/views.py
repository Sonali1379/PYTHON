from django.shortcuts import render
from rest_framework import viewsets
from myapp.models import *
from myapp.serializers import *


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

