from django.urls import path
from . import views

urlpatterns = [
    path('dash/', views.dash),
    path('', views.login),
    path('tags/', views.tags),
    path('clients/', views.cli),
    path('jobs/', views.jobs),
]