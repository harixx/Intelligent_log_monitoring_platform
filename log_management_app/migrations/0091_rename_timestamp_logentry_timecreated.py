# Generated by Django 5.1.2 on 2024-11-14 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log_management_app', '0090_logentry_event_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logentry',
            old_name='timestamp',
            new_name='TimeCreated',
        ),
    ]
