from rest_framework import serializers
from .models import Supermarket


class SupermarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supermarket
        fields = ('id', 'name', 'photo', 'address', 'open_state', 'operating_hours', 'website', 'distance')

