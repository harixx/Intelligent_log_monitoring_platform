# Generated by Django 4.2.11 on 2024-07-31 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_management_app', '0038_alter_windowsperflogs_log_source_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='windowsperflogs',
            name='log_source_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
