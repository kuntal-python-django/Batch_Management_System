# Generated by Django 2.2 on 2020-07-29 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_feedback_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]