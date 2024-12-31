from django.urls import path
from task5 import views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup_django/', views.sign_up_by_django, name='signup_django'),
    path('signup_html/', views.sign_up_by_html, name='signup_html'),
]