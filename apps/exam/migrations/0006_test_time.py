# Generated by Django 5.0.2 on 2024-12-13 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_test_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='time',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
