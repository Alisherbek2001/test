# Generated by Django 5.0.2 on 2024-12-13 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_alter_test_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='time',
            new_name='duration_test',
        ),
    ]