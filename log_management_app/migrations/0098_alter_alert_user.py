# Generated by Django 5.1.2 on 2024-11-20 00:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_management_app', '0097_alter_alert_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='user',
            field=models.ForeignKey(default='test', on_delete=django.db.models.deletion.CASCADE, related_name='alerts', to=settings.AUTH_USER_MODEL),
        ),
    ]