from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Listing
from .serializers import ListingSerializer
from rest_framework import filters
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status, viewsets
import pusher
import requests
from users.models import User
from users.serializers import GetUserSerializer

import json
from decouple import config
pusher_client = pusher.Pusher(
  app_id=config('pusher_id'),
  key=config('pusher_key'),
  secret=config('secret_key'),
  cluster='ap1',
  ssl=True
)
class ListingView(viewsets.ModelViewSet):
    queryset=Listing.objects.all()
    serializer_class=ListingSerializer
    def create(self,request):
        serializer = ListingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        url = f"https://graph.facebook.com/v12.0/100287059229982/feed?message=postman  and allow to message&access_token=EAAJvuShOAWoBACW8moTlaPn3BopnBCYAHdQg8JeREb51ZAXwumJ0y2JbQdTx3EuZBYq79FkWGufabobZBOwjhZBf69C3p4SyNWeexjH285uDMXRaXgQF1yLxbQF3o7NWP1qNEZAGc2tmnX69K929v5B9y6S7WaMBNZBMy49M392l3BXZCQ5c68Qm51KZCBRUQPYisH98TulUlLQIRNVpBv9k"

        payload = json.dumps({
        "message": f"{request.data.get('descriptions')}"
        })
        headers = {
        'Authorization': 'EAAJvuShOAWoBACW8moTlaPn3BopnBCYAHdQg8JeREb51ZAXwumJ0y2JbQdTx3EuZBYq79FkWGufabobZBOwjhZBf69C3p4SyNWeexjH285uDMXRaXgQF1yLxbQF3o7NWP1qNEZAGc2tmnX69K929v5B9y6S7WaMBNZBMy49M392l3BXZCQ5c68Qm51KZCBRUQPYisH98TulUlLQIRNVpBv9k',
        'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
        return Response(status=status.HTTP_200_OK)

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
            for x in items.data:
                    print('')
                    user = User.objects.filter(id=x['user_id'])
                    user = GetUserSerializer(user,many=True)
                    if(((user.data[0]['star_5'])+(user.data[0]['star_4'])+(user.data[0]['star_3'])+(user.data[0]['star_2'])+(user.data[0]['star_1']))==0):
                        x['rated']=0
                    else:
                        total_rate = (user.data[0]['star_5']*5)+(user.data[0]['star_4']*4)+(user.data[0]['star_3']*3)+(user.data[0]['star_2']*2)+(user.data[0]['star_1']*1)
                        total_quantity = ((user.data[0]['star_5'])+(user.data[0]['star_4'])+(user.data[0]['star_3'])+(user.data[0]['star_2'])+(user.data[0]['star_1']))
                        total = total_rate/total_quantity
                        print(total)
                        x['rated']=total
                        # print(((user.data[0]['star_5'])+(user.data[0]['star_4'])+(user.data[0]['star_3'])+(user.data[0]['star_2'])+(user.data[0]['star_1'])))
                    x['users']=user.data[0]
            return Response(status=status.HTTP_200_OK,data=items.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])



class Pusher(generics.GenericAPIView):
    permission_classes=[permissions.AllowAny]
    def post(self,request):
        pusher_client.trigger(request.data.get('channel'), 'my-test', {'message': 'hello world'})
        return Response()
        