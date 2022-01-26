from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Comments
from .serializers import CommentsSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
class CommentsView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Comments.objects.all()
    serializer_class=CommentsSerializer

class CommentsGetall(generics.GenericAPIView):
    queryset=Comments.objects.all()
    serializer_class=CommentsSerializer
    permission_classes=[permissions.AllowAny]
    def post(self,request):
        items = Comments.objects.filter(listing_id=request.data.get('listing_id'))
        items = CommentsSerializer(items,many=True)
        return Response(status=status.HTTP_200_OK,data=items.data)
        
