from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Custom user model for Vishubh EduBridge.
    """
    is_student = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)
    
    # Academic details
    # Using string references to avoid circular imports
    discipline = models.ForeignKey('academics.Discipline', on_delete=models.SET_NULL, null=True, blank=True)
    branch = models.ForeignKey('academics.Branch', on_delete=models.SET_NULL, null=True, blank=True)
    academic_year = models.ForeignKey('academics.AcademicYear', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username
