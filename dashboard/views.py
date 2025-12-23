from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from academics.models import Subject, StudyMaterial, Discipline
from .forms import SubjectForm, StudyMaterialForm

User = get_user_model()

class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class DashboardHomeView(StaffRequiredMixin, TemplateView):
    template_name = 'dashboard/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_students'] = User.objects.filter(is_staff=False).count()
        context['total_subjects'] = Subject.objects.count()
        context['total_materials'] = StudyMaterial.objects.count()
        context['disciplines'] = Discipline.objects.all()
        return context

# Subject Views
class SubjectListView(StaffRequiredMixin, ListView):
    model = Subject
    template_name = 'dashboard/subject_list.html'
    context_object_name = 'subjects'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        discipline_id = self.request.GET.get('discipline')
        if discipline_id:
            queryset = queryset.filter(branch__discipline_id=discipline_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        discipline_id = self.request.GET.get('discipline')
        if discipline_id:
            context['current_discipline'] = Discipline.objects.get(pk=discipline_id)
        return context

class SubjectCreateView(StaffRequiredMixin, CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'dashboard/subject_form.html'
    success_url = reverse_lazy('dashboard:subject_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        discipline_id = self.request.GET.get('discipline')
        if discipline_id:
            kwargs['initial'] = {'discipline_id': discipline_id}
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        discipline_id = self.request.GET.get('discipline')
        if discipline_id:
             context['current_discipline'] = Discipline.objects.get(pk=discipline_id)
        return context

class SubjectUpdateView(StaffRequiredMixin, UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'dashboard/subject_form.html'
    success_url = reverse_lazy('dashboard:subject_list')

class SubjectDeleteView(StaffRequiredMixin, DeleteView):
    model = Subject
    template_name = 'dashboard/subject_confirm_delete.html'
    success_url = reverse_lazy('dashboard:subject_list')

# Material Views
class MaterialListView(StaffRequiredMixin, ListView):
    model = StudyMaterial
    template_name = 'dashboard/material_list.html'
    context_object_name = 'materials'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        discipline_id = self.request.GET.get('discipline')
        if discipline_id:
            queryset = queryset.filter(subject__branch__discipline_id=discipline_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        discipline_id = self.request.GET.get('discipline')
        if discipline_id:
            context['current_discipline'] = Discipline.objects.get(pk=discipline_id)
        return context

class MaterialCreateView(StaffRequiredMixin, CreateView):
    model = StudyMaterial
    form_class = StudyMaterialForm
    template_name = 'dashboard/material_form.html'
    success_url = reverse_lazy('dashboard:material_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        discipline_id = self.request.GET.get('discipline')
        if discipline_id:
            kwargs['initial'] = {'discipline_id': discipline_id}
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        discipline_id = self.request.GET.get('discipline')
        if discipline_id:
             context['current_discipline'] = Discipline.objects.get(pk=discipline_id)
        return context

class MaterialUpdateView(StaffRequiredMixin, UpdateView):
    model = StudyMaterial
    form_class = StudyMaterialForm
    template_name = 'dashboard/material_form.html'
    success_url = reverse_lazy('dashboard:material_list')

class MaterialDeleteView(StaffRequiredMixin, DeleteView):
    model = StudyMaterial
    template_name = 'dashboard/material_confirm_delete.html'
    success_url = reverse_lazy('dashboard:material_list')
