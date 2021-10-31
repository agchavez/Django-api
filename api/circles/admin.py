from django.contrib import admin

from api.circles.models import Circles

@admin.register(Circles)
class CircleAdmin(admin.ModelAdmin):
    list_display = (
        'name','slug_name','about','rides_offered','rides_taken','verified','public','is_limit','member_limit'
    )

    search_fields = ('slug_name', 'name')

    list_filter = ('verified', 'public')