from rest_framework import serializers
from .models import Sold

class SoldSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sold
        fields="__all__"
