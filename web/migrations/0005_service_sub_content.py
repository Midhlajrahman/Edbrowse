# Generated by Django 5.0 on 2023-12-29 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='sub_content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
