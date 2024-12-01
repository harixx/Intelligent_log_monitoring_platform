# Generated by Django 5.1.2 on 2024-11-14 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_management_app', '0088_processlog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logentry',
            old_name='log_level',
            new_name='LevelDisplayName',
        ),
        migrations.AlterField(
            model_name='processlog',
            name='last_processed',
            field=models.DateTimeField(default=datetime.datetime(1, 1, 1, 0, 0)),
        ),
    ]