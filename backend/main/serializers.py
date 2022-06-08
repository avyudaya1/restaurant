from dataclasses import field
from rest_framework import serializers
from main.models import Item, ItemCategory, MenuItem, MenuItemCategory, Store

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("id", "name", "unit", "quantity", "manufacture_date", "expiry_date", "price")

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ("id", "name", "ingredients", "cooking_time", "cost", "menu_category")

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ("id", "name")

class MenuItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItemCategory
        fields = ("id", "name")

class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = ("id", "name")
