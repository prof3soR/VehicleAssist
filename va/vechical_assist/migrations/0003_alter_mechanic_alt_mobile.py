# Generated by Django 4.1.7 on 2023-03-25 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vechical_assist', '0002_mechanic_alt_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mechanic',
            name='alt_mobile',
            field=models.CharField(max_length=10),
        ),
    ]