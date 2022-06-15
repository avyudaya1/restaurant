from django.contrib import admin
from main.models import IngredientToMenuItem, Item, ItemCategory, MenuItem, MenuItemCategory, Store

# Register your models here.
admin.site.register(Item)
admin.site.register(ItemCategory)
admin.site.register(MenuItem)
admin.site.register(MenuItemCategory)
admin.site.register(Store)

class IngredientToMenuItemAdmin(admin.ModelAdmin):
    model = IngredientToMenuItem
    list_display = ['ingredient', 'menu_item']

admin.site.register(IngredientToMenuItem, IngredientToMenuItemAdmin)