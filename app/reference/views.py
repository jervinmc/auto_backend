from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Reference
from .serializers import ReferenceSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
class ReferenceView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Reference.objects.all()
    serializer_class=ReferenceSerializer

class ReferenceGetall(generics.GenericAPIView):
    queryset=Reference.objects.all()
    serializer_class=ReferenceSerializer
    permission_classes=[permissions.AllowAny]
    def get(self,request,format=None,email=None):
        try:
            items = Reference.objects.all()
            items = ReferenceSerializer(items,many=True)
            return Response(status=status.HTTP_200_OK,data=items.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])