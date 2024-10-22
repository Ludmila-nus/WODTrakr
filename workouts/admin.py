from django.contrib import admin

from workouts.models import Exercise, Routine, Workout, Goals, InjuryHistory, RestPeriod

@admin.register(Exercise)
class ExerciseResource(admin.ModelAdmin):
    model = Exercise
    list_display = ["name", "abbreviation"]

@admin.register(Routine)
class RoutineResource(admin.ModelAdmin):
    model = Routine
    list_display = ["user", "date", "notes"]    

@admin.register(Workout)
class WorkoutResource(admin.ModelAdmin):
    model = Workout
    list_display = ["exercise", "weight", "reps", "sets", "date", "notes"] 

@admin.register(Goals)
class GoalsResource(admin.ModelAdmin):
    model = Goals
    list_display = ["user", "exercise", "target_weight", "target_reps", "target_date"]

@admin.register(InjuryHistory)
class InjuryHistoryResource(admin.ModelAdmin):
    model = InjuryHistory
    list_display = ["user", "description", "date"] 

@admin.register(RestPeriod)
class RestPeriodResource(admin.ModelAdmin):
    model = RestPeriod
    list_display = ["user", "start_date", "end_date"]
