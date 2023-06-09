# Generated by Django 4.0.4 on 2023-05-02 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('screen_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('image', models.CharField(max_length=9999)),
            ],
        ),
    ]
