from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Listing
from .serializers import ListingSerializer
from rest_framework import filters
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status, viewsets
class ListingView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Listing.objects.all()
    serializer_class=ListingSerializer


class GetListingByUser(generics.GenericAPIView):
    queryset=Listing.objects.all()
    serializer_class=ListingSerializer
    def get(self,request):
        try:
            items=[]
            items=Listing.objects.filter(user_id=self.request.user.id)
            serializer=ListingSerializer(items,many=True)
            book_data = serializer.data
            return Response(data=book_data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])


class ListingGetall(generics.GenericAPIView):
    queryset=Listing.objects.all()
    serializer_class=ListingSerializer
    permission_classes=[permissions.AllowAny]
    def get(self,request,format=None,email=None):
        try:
            items = Listing.objects.all()
            items = ListingSerializer(items,many=True)
            return Response(status=status.HTTP_200_OK,data=items.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])