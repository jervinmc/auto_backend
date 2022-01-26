from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Sold
from .serializers import SoldSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
class SoldView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Sold.objects.all()
    serializer_class=SoldSerializer

class SoldGetall(generics.GenericAPIView):
    queryset=Sold.objects.all()
    serializer_class=SoldSerializer
    permission_classes=[permissions.AllowAny]
    def get(self,request,format=None,email=None):
        try:
            items = Sold.objects.all()
            items = SoldSerializer(items,many=True)
            return Response(status=status.HTTP_200_OK,data=items.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])
    
