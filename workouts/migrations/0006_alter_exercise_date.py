# Generated by Django 5.1 on 2024-10-30 14:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0005_alter_exercise_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]