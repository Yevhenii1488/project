from django.urls import path
from . import views

urlpatterns = [
    path('', views.participant_list, name='participant_list'),  # Main page for participants
    path('randomizer/', views.secret_santa_randomizer, name='secret_santa_randomizer'),  # Randomizer page
    path('clear/', views.clear_participants, name='clear_participants'),  # Clear participants
]
