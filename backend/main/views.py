from rest_framework import viewsets
from main.models import Item, ItemCategory, MenuItem, MenuItemCategory, Store
from main.serializers import ItemCategorySerializer, ItemSerializer, MenuItemCategorySerializer, MenuItemSerializer, StoreSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    search_fields = ["name"]

class ItemCategoryViewSet(viewsets.ModelViewSet):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
    search_fields = ["name"]

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    search_fields = ["name"]

class MenuItemCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuItemCategory.objects.all()
    serializer_class = MenuItemCategorySerializer
    search_fields = ["name"]

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    search_fields = ["name"]
