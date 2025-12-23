from django.urls import path
from . import views

app_name = 'academics'

urlpatterns = [
    path('discipline/<slug:discipline_slug>/', views.BranchListView.as_view(), name='branch_list'),
    path('branch/<slug:branch_slug>/', views.AcademicYearListView.as_view(), name='year_list'),
    path('branch/<slug:branch_slug>/year/<int:year>/', views.SubjectListView.as_view(), name='subject_list'),
    path('subject/<int:pk>/', views.SubjectDetailView.as_view(), name='subject_detail'),
    path('api/branches/<int:discipline_id>/', views.get_branches, name='get_branches'),
]
