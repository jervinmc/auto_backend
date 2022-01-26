from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Reports
from .serializers import ReportsSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
class ReportsView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Reports.objects.all()
    serializer_class=ReportsSerializer

class ReportsGetall(generics.GenericAPIView):
    queryset=Reports.objects.all()
    serializer_class=ReportsSerializer
    permission_classes=[permissions.AllowAny]
    
