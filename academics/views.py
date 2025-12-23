from django.views.generic import ListView, DetailView
from .models import Branch, AcademicYear, Subject, StudyMaterial
from django.shortcuts import get_object_or_404

class BranchListView(ListView):
    model = Branch
    template_name = 'academics/branch_list.html'
    context_object_name = 'branches'

    def get_queryset(self):
        discipline_slug = self.kwargs.get('discipline_slug')
        if discipline_slug:
            return Branch.objects.filter(discipline__slug=discipline_slug)
        return Branch.objects.all()

class AcademicYearListView(ListView):
    model = AcademicYear
    template_name = 'academics/year_list.html'
    context_object_name = 'years'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['branch'] = get_object_or_404(Branch, slug=self.kwargs.get('branch_slug'))
        return context

class SubjectListView(ListView):
    model = Subject
    template_name = 'academics/subject_list.html'
    context_object_name = 'subjects'

    def get_queryset(self):
        self.branch = get_object_or_404(Branch, slug=self.kwargs.get('branch_slug'))
        self.year = get_object_or_404(AcademicYear, year=self.kwargs.get('year'))
        return Subject.objects.filter(branch=self.branch, academic_year=self.year)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['branch'] = self.branch
        context['year'] = self.year
        return context

class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'academics/subject_detail.html'
    context_object_name = 'subject'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Group materials by type
        materials = self.object.materials.all()
        context['materials'] = materials

        # Parse Syllabus Text into Units
        syllabus_text = self.object.syllabus_text
        units = []
        if syllabus_text:
            # Split by '**Unit' which we used in populate_data
            parts = syllabus_text.split('**Unit')
            for part in parts:
                if not part.strip(): continue
                # Re-add 'Unit' prefix removed by split
                part = 'Unit' + part
                
                # Split title (first line) and content
                lines = part.strip().split('\n', 1)
                title = lines[0].strip().replace('**', '') # Remove bold markers
                content = lines[1].strip() if len(lines) > 1 else ""
                
                units.append({'title': title, 'content': content})
        
        context['syllabus_units'] = units
        return context

from django.http import JsonResponse
def get_branches(request, discipline_id):
    branches = Branch.objects.filter(discipline_id=discipline_id).values('id', 'name')
    return JsonResponse({'branches': list(branches)})
