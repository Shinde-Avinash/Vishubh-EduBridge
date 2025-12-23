from django import forms
from academics.models import Subject, StudyMaterial, Branch

from academics.models import Subject, StudyMaterial, Branch

class SubjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        discipline_id = initial.get('discipline_id')
        super().__init__(*args, **kwargs)
        if discipline_id:
            self.fields['branch'].queryset = Branch.objects.filter(discipline_id=discipline_id)
            
    class Meta:
        model = Subject
        fields = ['name', 'code', 'branch', 'academic_year', 'description', 'syllabus_text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject Name'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject Code'}),
            'branch': forms.Select(attrs={'class': 'form-control'}),
            'academic_year': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'syllabus_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Paste syllabus units here...'}),
        }

class StudyMaterialForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        discipline_id = initial.get('discipline_id')
        super().__init__(*args, **kwargs)
        if discipline_id:
            self.fields['subject'].queryset = Subject.objects.filter(branch__discipline_id=discipline_id)

    class Meta:
        model = StudyMaterial
        fields = ['title', 'type', 'subject', 'file', 'link', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Material Title'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'External Link (Optional)'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
