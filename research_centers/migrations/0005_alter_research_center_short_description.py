# Generated by Django 3.2.3 on 2021-07-22 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research_centers', '0004_research_center_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research_center',
            name='short_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
