# Generated by Django 5.1.2 on 2024-11-14 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_management_app', '0089_rename_log_level_logentry_leveldisplayname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='logentry',
            name='event_id',
            field=models.IntegerField(default=0),
        ),
    ]
