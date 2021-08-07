# Generated by Django 3.2.3 on 2021-08-07 18:21

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research_centers', '0014_alter_activity_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='video',
            field=models.TextField(blank=True, help_text='<b style="color:yellow;font-size: 12px">*IMPORTANT* Only add either Video link or Image, If you add both, only the image will be shown</b>', null=True),
        ),
        migrations.AlterField(
            model_name='research_center',
            name='image1',
            field=cloudinary.models.CloudinaryField(blank=True, help_text='<b style="color:yellow;font-size: 15px">*IMPORTANT* All three image should be of equal ratio (preffered: 3 x 2 )</b>', max_length=255, null=True, verbose_name='image1'),
        ),
    ]