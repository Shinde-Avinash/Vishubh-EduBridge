from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import StudentRegistrationForm
from django.contrib.auth import login

class RegisterView(CreateView):
    form_class = StudentRegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
