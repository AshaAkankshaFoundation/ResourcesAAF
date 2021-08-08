# Generated by Django 3.2.3 on 2021-08-07 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career_talks', '0011_alter_career_talk_short_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='career_talk',
            name='short_info',
        ),
        migrations.AddField(
            model_name='career_talk',
            name='short_description',
            field=models.TextField(blank=True, help_text='<b style="color:dodgerblue;font-size: 12px">Description of the card shown on all careers talk page. *MAX_Length = 250 characters"</b>', max_length=250, null=True),
        ),
    ]