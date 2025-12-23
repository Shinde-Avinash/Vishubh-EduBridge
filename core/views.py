from django.views.generic import TemplateView
from academics.models import Discipline

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            # If logged in, fetch relevant data for dashboard
            user = self.request.user
            if user.branch and user.academic_year:
                from academics.models import Subject
                context['subjects'] = Subject.objects.filter(
                    branch=user.branch,
                    academic_year=user.academic_year
                )
                context['dashboard'] = True
            else:
                # Fallback if profile incomplete
                context['disciplines'] = Discipline.objects.prefetch_related('branches').all()    
        else:
            context['disciplines'] = Discipline.objects.prefetch_related('branches').all()
        return context

class AboutView(TemplateView):
    template_name = 'about.html'

class CareersView(TemplateView):
    template_name = 'careers.html'
