# Generated by Django 3.2.3 on 2021-07-25 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research_centers', '0003_rename_photos_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='research_center',
            name='image',
        ),
    ]