from rest_framework import serializers
from main.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("id", "name", "unit", "quantity", "manufacture_date", "expiry_date", "price")