# Generated by Django 3.2.3 on 2021-08-07 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career_talks', '0006_auto_20210807_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='career_talk',
            name='short_info',
            field=models.CharField(blank=True, help_text='<b style="color:lightblue;font-size: 12px">Title of the card shown on careers talk page</b>', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='career_talk',
            name='embeded_video_link',
            field=models.TextField(blank=True, help_text='<b style="color:yellow;font-size: 12px">*IMPORTANT* Only add either Video link or Image, If you add both, only the image will be shown</b>', null=True),
        ),
    ]
