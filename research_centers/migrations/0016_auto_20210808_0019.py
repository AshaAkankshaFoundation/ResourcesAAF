# Generated by Django 3.2.3 on 2021-08-07 18:49

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research_centers', '0015_auto_20210807_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='video',
            field=models.TextField(blank=True, help_text='<b style="color:orange;font-size: 12px">*IMPORTANT* Only add either Video link or Image, If you add both, only the image will be shown</b>', null=True),
        ),
        migrations.AlterField(
            model_name='research_center',
            name='image1',
            field=cloudinary.models.CloudinaryField(blank=True, help_text='<b style="color:orange;font-size: 12px">*IMPORTANT* All three image should be of equal ratio (preffered: 3 x 2 )</b>', max_length=255, null=True, verbose_name='image1'),
        ),
        migrations.AlterField(
            model_name='research_center',
            name='join_us',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Join us link'),
        ),
        migrations.AlterField(
            model_name='research_center',
            name='short_description',
            field=models.TextField(blank=True, help_text='<b style="color:dodgerblue;font-size: 12px">Description of the card shown on all research centre page. *MAX_Length = 250 characters"</b>', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='research_center',
            name='video',
            field=models.CharField(blank=True, help_text='<b style="color:dodgerblue;font-size: 12px">Video that will we shown on join us card of research center</b>', max_length=500, null=True, verbose_name='Embeded Url'),
        ),
    ]