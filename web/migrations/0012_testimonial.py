# Generated by Django 5.0 on 2023-12-29 20:31

import versatileimagefield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_eventenquiry'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('designation', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('photo', versatileimagefield.fields.VersatileImageField(upload_to='testimonials/', verbose_name='Testimonial Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
            ],
            options={
                'verbose_name_plural': 'Testimonials',
            },
        ),
    ]
