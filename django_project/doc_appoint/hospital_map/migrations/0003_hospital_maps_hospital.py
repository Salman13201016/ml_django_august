# Generated by Django 4.2.5 on 2024-01-25 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_map', '0002_remove_hospital_maps_hos_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital_maps',
            name='hospital',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]