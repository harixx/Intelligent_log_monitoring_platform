# Generated by Django 5.1.2 on 2024-11-11 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log_management_app', '0075_rename_log_file_uploadedlog_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedlog',
            name='user',
        ),
    ]