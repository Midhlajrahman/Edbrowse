# Generated by Django 5.0.1 on 2024-02-19 13:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0005_alter_serviceenquiry_service"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="serviceenquiry",
            name="service",
        ),
    ]