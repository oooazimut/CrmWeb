# Generated by Django 5.0.6 on 2024-11-08 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supp', '0007_cars_carsinuse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carsinuse',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
