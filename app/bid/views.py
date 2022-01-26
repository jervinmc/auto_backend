from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Bid
from .serializers import BidSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
class BidView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Bid.objects.all()
    serializer_class=BidSerializer

class BidGetall(generics.GenericAPIView):
    queryset=Bid.objects.all()
    serializer_class=BidSerializer
    permission_classes=[permissions.AllowAny]
    def get(self,request,format=None,email=None):
        try:
            items = Bid.objects.all()
            items = BidSerializer(items,many=True)
            return Response(status=status.HTTP_200_OK,data=items.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])
    
