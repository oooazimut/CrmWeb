# Generated by Django 5.0.6 on 2024-11-08 10:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supp', '0006_alter_tasks_media_id_alter_tasks_resultid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.TextField(blank=True, null=True, verbose_name='Марка и модель')),
                ('state_number', models.TextField(blank=True, null=True, verbose_name='Госномер')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
                'db_table': 'cars',
            },
        ),
        migrations.CreateModel(
            name='CarsInUse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dttm', models.DateTimeField(blank=True, null=True, verbose_name='Время и дата')),
                ('car', models.ForeignKey(blank=True, db_column='car', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='supp.cars', verbose_name='Автомобиль')),
                ('user', models.ForeignKey(blank=True, db_column='user', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='supp.employees', verbose_name='Исполнитель')),
            ],
            options={
                'verbose_name': 'Закрепленный автомобиль',
                'verbose_name_plural': 'Закрепленные автомобили',
                'db_table': 'cars_in_use',
            },
        ),
    ]
