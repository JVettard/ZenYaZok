from django.db import models

class Membre(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    date_naissance = models.DateField()

    def __str__(self):
        return self.nom


