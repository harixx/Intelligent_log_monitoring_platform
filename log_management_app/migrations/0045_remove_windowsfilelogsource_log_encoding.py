# Generated by Django 4.2.11 on 2024-08-01 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log_management_app', '0044_windowsactivedirectorylogsource_collection_mtd_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='windowsfilelogsource',
            name='log_encoding',
        ),
    ]