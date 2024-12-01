# Generated by Django 4.2.11 on 2024-08-15 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_management_app', '0067_linuxfilelogsource_log_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebServer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
