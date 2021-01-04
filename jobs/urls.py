from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('work', views.work, name = 'work'),
    path('projects', views.projects, name = 'projects'),
    path('contact/', views.contact, name = 'contact'),
    path('submit', views.submit, name='submit'),
]