# Generated by Django 4.0 on 2022-02-05 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0005_rename_measurement_id_measurement_station_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='street',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]