# Generated by Django 5.1.2 on 2024-11-12 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_management_app', '0082_maclogfile_delete_ldaplogsource_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApacheLogFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_name', models.CharField(blank=True, max_length=20, null=True)),
                ('os_type', models.CharField(default='apache', max_length=50)),
                ('file', models.FileField(upload_to='uploaded_logs/apache/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ApacheLogFileUploadForm',
        ),
        migrations.DeleteModel(
            name='ApacheserverLogFileStream',
        ),
        migrations.DeleteModel(
            name='ApacheserverLogStream',
        ),
        migrations.DeleteModel(
            name='ApacheserverPerfLogs',
        ),
        migrations.DeleteModel(
            name='MacFileLogSource',
        ),
        migrations.RemoveField(
            model_name='maclogsource',
            name='log_type',
        ),
        migrations.DeleteModel(
            name='MacPerformanceMetric',
        ),
        migrations.DeleteModel(
            name='OpenDirLogSource',
        ),
        migrations.DeleteModel(
            name='WebServer',
        ),
        migrations.DeleteModel(
            name='MacLogSource',
        ),
        migrations.DeleteModel(
            name='MacLogType',
        ),
    ]