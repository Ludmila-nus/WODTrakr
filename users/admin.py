from django.contrib import admin

from .models import UserProfile, UserPreferences

@admin.register(UserProfile)
class UserProfileResource(admin.ModelAdmin):
    model = UserProfile
    list_display = ("user", "full_name", "created_at")

@admin.register(UserPreferences)
class UserPreferencesResource(admin.ModelAdmin):
    model = UserPreferences
    list_display = ("user", "dark_mode", "language")