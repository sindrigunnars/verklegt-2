# Generated by Django 4.0.4 on 2023-05-02 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='pizzatype',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
