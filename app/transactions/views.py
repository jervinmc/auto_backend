from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Transactions
from .serializers import TransactionsSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
from listing.models import Listing
from sold.models import Sold
from users.models import User
class TransactionsView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Transactions.objects.all()
    serializer_class=TransactionsSerializer
    def list(self,request):
        try:
            items = Transactions.objects.filter(user_id = self.request.user.id)
            items = TransactionsSerializer(items,many=True)
            return Response(status=status.HTTP_200_OK,data=items.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])

class TransactionsGetall(generics.GenericAPIView):
    queryset=Transactions.objects.all()
    serializer_class=TransactionsSerializer
    permission_classes=[permissions.AllowAny]
    def get(self,request,format=None,email=None):
        try:
            items = Transactions.objects.all()
            items = TransactionsSerializer(items,many=True)
            return Response(status=status.HTTP_200_OK,data=items.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])



class GetSales(generics.GenericAPIView):
    def get(self,request,page=None):
            if(self.request.user.account_type=='Seller'):
                no_listing=Listing.objects.filter(user_id=self.request.user.id).count()
                no_sold= Sold.objects.filter(user_id=self.request.user.id).count()
                return Response(status=status.HTTP_200_OK,data={"no_listing":no_listing,"no_sold":no_sold})
            elif(self.request.user.account_type=='Customer'):
                return Response(status=status.HTTP_200_OK,data={})
            else:
                no_seller=User.objects.filter(account_type='Seller').count()
                no_customer= User.objects.filter(account_type='Customer').count()
                return Response(status=status.HTTP_200_OK,data={"no_seller":no_seller,"no_customer":no_customer})
