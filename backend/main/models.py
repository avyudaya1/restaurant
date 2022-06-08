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
    unit_choices = ([0, 'Kilogram'], [1, 'Litre'],)
    unit = models.IntegerField(choices=unit_choices)
    quantity = models.FloatField(validators=[MinValueValidator(0.0)])
    manufacture_date = models.DateField()
    expiry_date = models.DateField()
    item_category = models.ForeignKey(ItemCategory, blank=False, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class MenuItemCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Menu item Categories'
    
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Item)
    cooking_time = models.TimeField()
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