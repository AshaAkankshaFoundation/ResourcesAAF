# Generated by Django 3.2.3 on 2021-08-07 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20210808_0019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='short_description',
        ),
    ]
