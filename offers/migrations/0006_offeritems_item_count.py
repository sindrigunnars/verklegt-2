# Generated by Django 4.0.4 on 2023-05-02 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0005_remove_offer_items_offeritems'),
    ]

    operations = [
        migrations.AddField(
            model_name='offeritems',
            name='item_count',
            field=models.PositiveIntegerField(default=1, verbose_name=72),
        ),
    ]
