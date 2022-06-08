from django.contrib import admin
from main.models import Item, ItemCategory, MenuItem, MenuItemCategory, Store

# Register your models here.
admin.site.register(Item)
admin.site.register(ItemCategory)
admin.site.register(MenuItem)
admin.site.register(MenuItemCategory)
admin.site.register(Store)