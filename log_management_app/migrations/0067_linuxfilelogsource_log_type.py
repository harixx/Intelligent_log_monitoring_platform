# Generated by Django 4.2.11 on 2024-08-15 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_management_app', '0066_alter_windowsfilelogsource_ingestion_mtd'),
    ]

    operations = [
        migrations.AddField(
            model_name='linuxfilelogsource',
            name='log_type',
            field=models.ManyToManyField(to='log_management_app.linuxlogtype'),
        ),
    ]