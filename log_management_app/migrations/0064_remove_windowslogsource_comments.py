# Generated by Django 4.2.11 on 2024-08-12 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log_management_app', '0063_alter_windowslogtype_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='windowslogsource',
            name='comments',
        ),
    ]
