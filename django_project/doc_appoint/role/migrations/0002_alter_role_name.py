# Generated by Django 4.2 on 2023-10-23 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("role", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="role",
            name="name",
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
