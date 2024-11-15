# Generated by Django 5.1 on 2024-11-08 14:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0007_knownworkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='routine',
            name='type',
            field=models.CharField(choices=[('for_time', 'For Time'), ('amrap', 'AMRAP'), ('emom', 'EMOM'), ('rft', 'Rounds for Time'), ('chipper', 'Chipper'), ('endurance', 'Endurance'), ('tabata', 'Tabata')], default='for_time', max_length=20),
        ),
        migrations.AddField(
            model_name='workout',
            name='time',
            field=models.DurationField(blank=True, help_text='Duration in minutes:seconds', null=True),
        ),
        migrations.AlterField(
            model_name='workout',
            name='reps',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workout',
            name='rounds',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='workout',
            name='routine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workout', to='workouts.routine'),
        ),
        migrations.AlterField(
            model_name='workout',
            name='sets',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workout',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
