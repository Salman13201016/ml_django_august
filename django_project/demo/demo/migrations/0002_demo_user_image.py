# Generated by Django 4.2 on 2023-10-09 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demo", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="demo_user",
            name="image",
            field=models.ImageField(default=1, upload_to="images/"),
            preserve_default=False,
        ),
    ]