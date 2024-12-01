# Generated by Django 4.2.11 on 2024-07-31 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_management_app', '0042_alter_windowsperflogs_log_source_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='windowsactivedirectorylogsource',
            name='domain_controller_ip',
        ),
        migrations.RemoveField(
            model_name='windowsactivedirectorylogsource',
            name='log_format',
        ),
        migrations.RemoveField(
            model_name='windowsactivedirectorylogsource',
            name='log_level',
        ),
        migrations.RemoveField(
            model_name='windowsactivedirectorylogsource',
            name='password',
        ),
        migrations.RemoveField(
            model_name='windowsactivedirectorylogsource',
            name='port_number',
        ),
        migrations.RemoveField(
            model_name='windowsactivedirectorylogsource',
            name='retention_period',
        ),
        migrations.RemoveField(
            model_name='windowsactivedirectorylogsource',
            name='username',
        ),
        migrations.AddField(
            model_name='windowsactivedirectorylogsource',
            name='activate',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='windowsactivedirectorylogsource',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='windowsactivedirectorylogsource',
            name='hostname_ip_address',
            field=models.CharField(default='localhost', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='windowsactivedirectorylogsource',
            name='ingestion_mtd',
            field=models.CharField(default='powershell', max_length=30),
        ),
        migrations.AddField(
            model_name='windowsactivedirectorylogsource',
            name='retention_policy',
            field=models.CharField(choices=[('7d', '7 days'), ('14d', '14 days'), ('30d', '30 days'), ('60d', '60 days'), ('90d', '90 days'), ('180d', '180 days'), ('365d', '365 days')], default='30d', max_length=10),
        ),
        migrations.AddField(
            model_name='windowsactivedirectorylogsource',
            name='status',
            field=models.CharField(choices=[('Online', 'Active'), ('Offline', 'Inactive')], default='Offline', max_length=10),
        ),
        migrations.AddField(
            model_name='windowsactivedirectorylogsource',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='windowsactivedirectorylogsource',
            name='collection_interval',
            field=models.CharField(choices=[('5m', 'Every 5 minutes'), ('15m', 'Every 15 minutes'), ('30m', 'Every 30 minutes'), ('1h', 'Every 1 hour'), ('6h', 'Every 6 hours'), ('12h', 'Every 12 hours'), ('24h', 'Every 24 hours')], default='24h', max_length=10),
        ),
    ]
