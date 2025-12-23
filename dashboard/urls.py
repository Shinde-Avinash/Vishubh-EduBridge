from django.urls import path
from .views import (
    DashboardHomeView,
    SubjectListView, SubjectCreateView, SubjectUpdateView, SubjectDeleteView,
    MaterialListView, MaterialCreateView, MaterialUpdateView, MaterialDeleteView
)

app_name = 'dashboard'

urlpatterns = [
    path('', DashboardHomeView.as_view(), name='home'),
    
    # Subject URLs
    path('subjects/', SubjectListView.as_view(), name='subject_list'),
    path('subjects/add/', SubjectCreateView.as_view(), name='subject_add'),
    path('subjects/<int:pk>/edit/', SubjectUpdateView.as_view(), name='subject_edit'),
    path('subjects/<int:pk>/delete/', SubjectDeleteView.as_view(), name='subject_delete'),

    # Material URLs
    path('materials/', MaterialListView.as_view(), name='material_list'),
    path('materials/add/', MaterialCreateView.as_view(), name='material_add'),
    path('materials/<int:pk>/edit/', MaterialUpdateView.as_view(), name='material_edit'),
    path('materials/<int:pk>/delete/', MaterialDeleteView.as_view(), name='material_delete'),
]
