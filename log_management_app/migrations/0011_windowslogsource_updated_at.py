# Generated by Django 3.2.8 on 2024-07-15 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_management_app', '0010_auto_20240715_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='windowslogsource',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
