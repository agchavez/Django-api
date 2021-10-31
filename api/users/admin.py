"""Modelo para usuarios administradores """

#Django 
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#Models 
from api.users.models import User, Client

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name')
    list_filter = ('is_staff', 'created', 'modified')

@admin.register(Client)
class PorfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'reputation', 'rides_offered','rides_taken' )
    search_filds = ('user__username', 'user__email', 'user__first_name')
    list_filter = ('reputation','rides_offered')

admin.site.register(User, CustomUserAdmin)