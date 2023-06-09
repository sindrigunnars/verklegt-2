# Generated by Django 4.0.4 on 2023-05-02 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_pizza_type'),
        ('offers', '0008_remove_offeritems_count_item_alter_offeritems_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offeritems',
            name='items',
        ),
        migrations.RemoveField(
            model_name='offeritems',
            name='offer',
        ),
        migrations.AddField(
            model_name='offer',
            name='items',
            field=models.ManyToManyField(to='menu.pizza'),
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='OfferItems',
        ),
    ]
