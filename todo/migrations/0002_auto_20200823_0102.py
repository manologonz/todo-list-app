# Generated by Django 3.1 on 2020-08-23 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
