# Generated by Django 4.2 on 2023-11-06 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("role", "0002_alter_role_name"),
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="Role", new_name="User",),
    ]
