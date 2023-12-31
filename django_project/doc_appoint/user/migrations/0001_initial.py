# Generated by Django 4.2 on 2023-11-06 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("role", "0002_alter_role_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=500)),
                ("email", models.CharField(max_length=500)),
                ("phone", models.CharField(max_length=500)),
                ("address", models.TextField()),
                ("pw", models.CharField(max_length=500)),
                (
                    "role_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="role.role"
                    ),
                ),
            ],
        ),
    ]
