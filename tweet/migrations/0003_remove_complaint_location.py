# Generated by Django 5.1.6 on 2025-03-01 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_complaint_latitude_complaint_longitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='location',
        ),
    ]
