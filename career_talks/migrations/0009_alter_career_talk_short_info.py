# Generated by Django 3.2.3 on 2021-08-07 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career_talks', '0008_auto_20210807_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career_talk',
            name='short_info',
            field=models.TextField(blank=True, help_text='<b style="color:dodgerblue;font-size: 12px">Title of the card shown on careers talk page. *MAX_Length = 500characters"</b>', max_length=300, null=True),
        ),
    ]
