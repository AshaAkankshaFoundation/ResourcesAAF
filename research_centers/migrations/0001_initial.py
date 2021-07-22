# Generated by Django 3.2.3 on 2021-07-21 22:51

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Research_Center',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image_url', models.CharField(max_length=250)),
                ('info', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image_url', models.CharField(max_length=250)),
                ('text', ckeditor.fields.RichTextField()),
                ('research_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='research_centers.research_center')),
            ],
        ),
    ]
