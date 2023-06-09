# Generated by Django 4.0.4 on 2023-05-02 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_pizza_name_alter_pizzatype_name'),
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='image',
            field=models.CharField(blank=True, max_length=9999),
        ),
        migrations.AlterField(
            model_name='offer',
            name='items',
            field=models.ManyToManyField(null=True, to='menu.pizza'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
