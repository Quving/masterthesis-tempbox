# Generated by Django 4.0 on 2021-12-21 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='source',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
