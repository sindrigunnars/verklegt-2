# Generated by Django 4.0.4 on 2023-05-03 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_pizza_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizzaimage',
            name='pizza',
        ),
        migrations.AddField(
            model_name='pizza',
            name='images',
            field=models.ManyToManyField(to='menu.pizzaimage'),
        ),
    ]
