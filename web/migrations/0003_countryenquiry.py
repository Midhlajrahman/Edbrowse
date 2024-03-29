# Generated by Django 5.0.1 on 2024-02-19 12:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0002_eventenquiry_is_accepted"),
    ]

    operations = [
        migrations.CreateModel(
            name="CountryEnquiry",
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
                ("name", models.CharField(max_length=250)),
                ("email", models.EmailField(max_length=250)),
                ("phone", models.CharField(max_length=250)),
                ("subject", models.CharField(max_length=250)),
                ("message", models.TextField()),
            ],
        ),
    ]
