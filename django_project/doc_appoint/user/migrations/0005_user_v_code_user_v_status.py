# Generated by Django 4.2 on 2023-11-22 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_remove_user_v_code_remove_user_v_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="v_code",
            field=models.CharField(default=1, max_length=500, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="v_status",
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
