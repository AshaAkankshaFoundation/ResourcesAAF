# Generated by Django 3.2.3 on 2021-07-25 12:08

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research_centers', '0005_activity_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='research_center',
            name='image1',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='research_center',
            name='image2',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='research_center',
            name='image3',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
