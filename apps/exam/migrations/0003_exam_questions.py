# Generated by Django 5.0.2 on 2024-12-06 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_exam_count_question_exam_score'),
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='questions',
            field=models.ManyToManyField(blank=True, to='question.question'),
        ),
    ]
