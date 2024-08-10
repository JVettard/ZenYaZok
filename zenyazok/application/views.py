from django.shortcuts import render
from .models import Membre

def accueil(request):
    membres = Membre.objects.all()
    return render(request, 'application/accueil.html', {'membres': membres})