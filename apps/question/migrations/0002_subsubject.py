# Generated by Django 5.0.2 on 2024-12-13 05:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.subject')),
            ],
            options={
                'verbose_name': 'SubSubject',
                'verbose_name_plural': 'SubSubjects',
            },
        ),
    ]
