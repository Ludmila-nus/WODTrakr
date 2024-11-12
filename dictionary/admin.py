from django.contrib import admin

from dictionary.models import Term

@admin.register(Term)
class TermResource(admin.ModelAdmin):
    model = Term
    list_display = ["category", "term", "definition"]
