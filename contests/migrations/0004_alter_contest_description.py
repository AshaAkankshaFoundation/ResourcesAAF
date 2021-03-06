# Generated by Django 3.2.3 on 2021-08-07 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0003_alter_contest_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='description',
            field=models.TextField(blank=True, help_text='<b style="color:dodgerblue;font-size: 12px">Description of the card shown on all contests page. *MAX_Length = 250 characters"</b>', max_length=250, null=True, verbose_name='short description'),
        ),
    ]
