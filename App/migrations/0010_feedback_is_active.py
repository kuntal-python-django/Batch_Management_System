# Generated by Django 2.2 on 2020-07-30 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_batch_attendance_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
