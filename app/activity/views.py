from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Activity
from .serializers import ActivitySerializer
from rest_framework import filters
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status, viewsets
class ActivityView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Activity.objects.all()
    serializer_class=ActivitySerializer
    
    def list(self,request):
        try:
            items = Activity.objects.filter(user_id = self.request.user.id)
            items = ActivitySerializer(items,many=True)
            return Response(status=status.HTTP_200_OK,data=items.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])
