from django.db import models

class Discipline(models.Model):
    """
    Broad field of study (e.g., Engineering, Science, Commerce).
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Disciplines"

class Branch(models.Model):
    """
    Specific stream within a discipline (e.g., CSE, IT, BCom, BSc Physics).
    """
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, related_name='branches')
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.discipline.name})"

    class Meta:
        verbose_name_plural = "Branches"

class AcademicYear(models.Model):
    """
    Year of study (1st Year, 2nd Year, etc.).
    """
    year = models.IntegerField(unique=True) # 1, 2, 3...
    name = models.CharField(max_length=50) # "First Year"

    def __str__(self):
        return self.name

class Subject(models.Model):
    """
    Subjects taught in a specific branch and year.
    """
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='subjects')
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE, related_name='subjects')
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)
    syllabus_text = models.TextField(blank=True, help_text="Paste syllabus content here")

    def __str__(self):
        return f"{self.name} - {self.branch.name} ({self.academic_year})"

class StudyMaterial(models.Model):
    """
    Resources for a subject.
    """
    MATERIAL_TYPES = [
        ('syllabus', 'Syllabus PDF'),
        ('video', 'Video Lecture'),
        ('book', 'eBook'),
        ('note', 'Notes'),
        ('reference', 'Reference Link'),
    ]
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='materials')
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=MATERIAL_TYPES)
    file = models.FileField(upload_to='materials/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_type_display()})"
