# Generated by Django 5.0.1 on 2024-02-19 13:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0009_courseenquiry_delete_enquiry"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="courseenquiry",
            options={"verbose_name_plural": "Course Enquiries"},
        ),
    ]
