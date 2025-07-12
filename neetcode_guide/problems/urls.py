from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('problem/<int:problem_id>/', views.problem_detail, name='problem_detail'),
    path('stats/', views.stats, name='stats')
]