from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login),
    path('productos', views.productos),
    path('customer', views.customer),
   

]