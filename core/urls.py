from django.urls import path
from .views import ProjectDetailView
from . import views
from .views import HomeView, AboutView, SkillsView, ProjectsView, ContactView, ProjectListView 

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('about/', AboutView.as_view(), name='about'),
    path('skills/', SkillsView.as_view(), name='skills'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('resume/view/', views.resume_view, name='resume_view'),
    path('<slug:slug>/', ProjectDetailView.as_view(), name='project_detail'),
   
]
