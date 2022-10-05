from django.shortcuts import render
from . serializers import RegisterSerializer
from rest_framework import viewsets
from . models import Register
# Create your views here.

class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

