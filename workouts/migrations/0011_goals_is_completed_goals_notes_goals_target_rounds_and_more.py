# Generated by Django 5.1 on 2025-01-08 01:14

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0010_alter_exercise_abbreviation_alter_exercise_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='goals',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='goals',
            name='notes',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='goals',
            name='target_rounds',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='goals',
            name='target_sets',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='goals',
            name='target_time',
            field=models.DurationField(blank=True, help_text='Duration in minutes:seconds', null=True),
        ),
    ]
