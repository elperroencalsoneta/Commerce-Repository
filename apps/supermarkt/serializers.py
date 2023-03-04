from rest_framework import serializers
from .models import Supermarkt


class SupermarktSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supermarkt
        fields = ('id', 'name', 'photo', 'address', 'open_state', 'operating_hours', 'website', 'distance')

