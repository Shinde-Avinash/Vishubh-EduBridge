from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Academic Info', {'fields': ('is_student', 'is_faculty', 'discipline', 'branch', 'academic_year')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'discipline', 'branch', 'academic_year')
    list_filter = ('is_student', 'is_faculty', 'discipline', 'branch', 'academic_year')
