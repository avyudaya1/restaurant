# Generated by Django 4.0.5 on 2022-06-08 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_menucategory_menuitemcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='itemcategory',
            options={'verbose_name_plural': 'Item Categories'},
        ),
        migrations.AlterModelOptions(
            name='menuitemcategory',
            options={'verbose_name_plural': 'Menu item Categories'},
        ),
    ]