# Generated by Django 4.1.7 on 2023-03-25 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vechical_assist', '0003_alter_mechanic_alt_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='mechanic',
            name='car_company',
            field=models.CharField(default='car', max_length=100),
            preserve_default=False,
        ),
    ]