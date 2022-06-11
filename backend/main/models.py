from calendar import c
from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.core.validators import MinValueValidator
from django.forms import ValidationError

class ItemCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Item Categories'
    
    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    unit_choices = (['Kilogram', 'Kilogram'], ['Litre', 'Litre'],)
    unit = models.CharField(choices=unit_choices, max_length=20)
    quantity = models.FloatField(validators=[MinValueValidator(0.0)])
    manufacture_date = models.DateField()
    expiry_date = models.DateField()
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    item_category = models.ForeignKey(ItemCategory, blank=False, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        if Item.objects.filter(name=self.name).exists():
            raise ValidationError(self.name, ' already exists. Edit it.')
        if self.manufacture_date > self.expiry_date:
            raise ValidationError('The expiry date can not be earlier than manufacture date.')
        elif self.manufacture_date == self.expiry_date:
            raise ValidationError('Manufacture and Expiry dates can not be same.')
        return super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class MenuItemCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Menu item Categories'
    
    def __str__(self):
        return self.name 

class IngredientToMenuItem(models.Model):
    ingredient = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.FloatField(validators=[MinValueValidator(0.0)])
    menu_item = models.ForeignKey("main.MenuItem", on_delete=models.CASCADE)

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Item, through="main.IngredientToMenuItem")
    cooking_time = models.DurationField()
    cost = models.FloatField(validators=[MinValueValidator(0.0)])
    menu_category = models.ForeignKey(MenuItemCategory, blank=False, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Store'

    def save(self, *args, **kwargs):
        if not self.pk and Store.objects.exists():
            raise ValidationError('There is can be only one Store instance')
        return super(Store, self).save(*args, **kwargs)