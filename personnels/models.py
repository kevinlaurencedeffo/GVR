from django.db import models


class Perso(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    matricule = models.CharField(max_length=100)
    cni = models.CharField(max_length=100)
    nationalite = models.CharField(max_length=100)
    email = models.EmailField()
    sexe = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    poste = models.CharField(max_length=100)
    quartier = models.CharField(max_length=100)
    tel = models.IntegerField(default=0)
    
    
    
    def __str__(self):
        return self.name

class Task(models.Model):
    nom=models.CharField(max_length=100)
    montant=models.DecimalField(max_digits=15, decimal_places=2,default=0)
    service=models.CharField(max_length=500)
    etat=models.CharField(max_length=100)
    chef_projet=models.CharField(max_length=100)
    date_debut=models.DateField()
    date_fin=models.DateField()
    def __str__(self):
        return self.nom
    
