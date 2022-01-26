from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Swap
from .serializers import SwapSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
class SwapView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Swap.objects.all()
    serializer_class=SwapSerializer

class SwapGetall(generics.GenericAPIView):
    queryset=Swap.objects.all()
    serializer_class=SwapSerializer
    permission_classes=[permissions.AllowAny]
    def get(self,request,format=None,email=None):
        try:
            items = Swap.objects.filter(user_id=self.request.user.id)
            items = SwapSerializer(items,many=True)
            return Response(status=status.HTTP_200_OK,data=items.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])