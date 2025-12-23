from django.db import models

class CareerOpportunity(models.Model):
    """
    Guidance on career paths for a specific branch.
    """
    branch = models.ForeignKey('academics.Branch', on_delete=models.CASCADE, related_name='career_opportunities')
    title = models.CharField(max_length=200) 
    description = models.TextField()
    skills_required = models.TextField(help_text="Comma separated or list of skills")
    average_salary = models.CharField(max_length=100, blank=True)
    
    class Meta:
        verbose_name_plural = "Career Opportunities"

    def __str__(self):
        return self.title

class ProjectIdea(models.Model):
    """
    Project ideas for students.
    """
    DIFFICULTY_LEVELS = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]
    
    branch = models.ForeignKey('academics.Branch', on_delete=models.CASCADE, related_name='project_ideas')
    academic_year = models.ForeignKey('academics.AcademicYear', on_delete=models.CASCADE, related_name='project_ideas')
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_LEVELS)
    technologies = models.CharField(max_length=200, help_text="e.g. Python, Django, React")
    
    def __str__(self):
        return self.title
