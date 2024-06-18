# Generated by Django 5.0.6 on 2024-06-15 17:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("project_number", models.CharField(max_length=100, unique=True)),
                ("project_title", models.CharField(max_length=200)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("scope_of_work", models.TextField()),
                ("approved_hours", models.IntegerField()),
                ("product_number", models.CharField(max_length=100)),
                ("trigger", models.CharField(max_length=200)),
                ("client_name", models.CharField(max_length=200)),
                (
                    "project_leader",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
