# Generated by Django 4.1.7 on 2023-03-28 05:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vechical_assist', '0006_alter_service_request_lat_alter_service_request_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='service_request',
            name='dateandtime',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]