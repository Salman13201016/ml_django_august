# Generated by Django 4.2 on 2023-11-13 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("role", "0002_alter_role_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="role",
            name="name2",
            field=models.CharField(default=None, max_length=500),
            preserve_default=False,
        ),
    ]
