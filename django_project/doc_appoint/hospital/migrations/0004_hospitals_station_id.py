# Generated by Django 4.2.5 on 2024-01-25 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0001_initial'),
        ('hospital', '0003_remove_hospitals_station_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospitals',
            name='station_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='station.stations'),
            preserve_default=False,
        ),
    ]
