# Generated by Django 4.0.4 on 2023-05-09 11:11

import creditcards.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0012_alter_paymentinformation_card_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinformation',
            name='zip',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(9999)]),
        ),
        migrations.AlterField(
            model_name='paymentinformation',
            name='card_number',
            field=creditcards.models.CardNumberField(max_length=25, verbose_name='card number'),
        ),
        migrations.AlterField(
            model_name='paymentinformation',
            name='cvc',
            field=creditcards.models.SecurityCodeField(max_length=4, verbose_name='security code'),
        ),
        migrations.AlterField(
            model_name='paymentinformation',
            name='expiry',
            field=creditcards.models.CardExpiryField(verbose_name='expiration date'),
        ),
    ]
