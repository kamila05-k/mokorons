# Generated by Django 5.0.7 on 2024-08-02 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_component_options_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='component',
            options={'verbose_name': 'Компонент', 'verbose_name_plural': 'Компоненты'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Карточка товара', 'verbose_name_plural': 'Карточки товаров'},
        ),
    ]