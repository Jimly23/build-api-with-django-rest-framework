from django.shortcuts import render
from rest_framework import viewsets
from .models import Kontak
from .serializer import KontakSerializer


# Create your views here.
class KontakViewset(viewsets.ModelViewSet):
    queryset = Kontak.objects.all()
    serializer_class = KontakSerializer