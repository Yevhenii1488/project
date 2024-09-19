from django.urls import path
from . import views

urlpatterns = [
    path('', views.is_it_christmas, name='is_it_christmas'),
]
