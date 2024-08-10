from django.urls import path
from . import views
from .views import accueil	

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('accueil/', views.accueil, name='accueil'),
]