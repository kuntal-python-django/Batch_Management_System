# Generated by Django 2.2 on 2020-07-29 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.IntegerField(choices=[(1, 'E'), (2, 'A+'), (3, 'A'), (4, 'B+'), (5, 'B'), (6, 'C'), (7, 'NA')], default=7),
        ),
    ]
