from django.contrib import admin
from .models import Discipline, Branch, AcademicYear, Subject, StudyMaterial

@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'discipline', 'slug')
    list_filter = ('discipline',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ('name', 'year')
    ordering = ('year',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'branch', 'academic_year')
    list_filter = ('branch', 'academic_year')
    search_fields = ('name', 'code')

@admin.register(StudyMaterial)
class StudyMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'subject', 'created_at')
    list_filter = ('type', 'subject__branch', 'subject__academic_year')
    search_fields = ('title', 'description')
