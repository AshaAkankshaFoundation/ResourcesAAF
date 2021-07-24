# Generated by Django 3.2.3 on 2021-07-24 10:16

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career_talks', '0008_auto_20210703_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career_talk',
            name='image_url',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
    ]
