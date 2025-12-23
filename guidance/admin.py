from django.contrib import admin
from .models import CareerOpportunity, ProjectIdea

@admin.register(CareerOpportunity)
class CareerOpportunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'branch', 'average_salary')
    list_filter = ('branch',)
    search_fields = ('title', 'description')

@admin.register(ProjectIdea)
class ProjectIdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty', 'branch', 'academic_year')
    list_filter = ('difficulty', 'branch', 'academic_year')
    search_fields = ('title', 'technologies')
