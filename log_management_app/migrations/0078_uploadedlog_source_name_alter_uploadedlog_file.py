# Generated by Django 5.1.2 on 2024-11-12 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_management_app', '0077_remove_logentry_log_file_delete_anomaly'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedlog',
            name='source_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='uploadedlog',
            name='file',
            field=models.FileField(upload_to='uploaded_logs/windows/'),
        ),
    ]