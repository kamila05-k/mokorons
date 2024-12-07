# Generated by Django 5.0.7 on 2024-08-15 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wedding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Изображение')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('available', models.BooleanField(default=True, verbose_name='В наличии')),
                ('in_cart', models.BooleanField(default=False, verbose_name='В корзине')),
            ],
            options={
                'verbose_name': 'Свадьба',
                'verbose_name_plural': 'Свадьбы',
            },
        ),
    ]
