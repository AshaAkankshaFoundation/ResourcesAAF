# Generated by Django 3.2.3 on 2021-07-21 18:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contests', '0020_auto_20210721_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]