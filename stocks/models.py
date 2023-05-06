from django.db import models
import datetime, random

class Stocks(models.Model):
    article_name = models.CharField(max_length=100)
    libele = models.TextField()
    quantite = models.IntegerField(default=0)
    prix = models.DecimalField(max_digits=15, decimal_places=2,default=0)
    date = models.CharField(max_length=100)
    img = models.ImageField(upload_to="media", blank=True)
    typea = models.CharField(max_length=100)
    si = models.IntegerField(default=0)
    def __str__(self):
        return self.article_name
    
    def mnt(self):
        montant = float(self.prix)*float(self.quantite)
        return montant

    def soldef(self):
        sr=0
        en=0
        if self.typea == "Entree":
            en=self.prix
            sf = int(self.si)+int(en)
        elif self.typea == "Sortie":
            sr = self.prix
            sf = int(self.si)-int(sr)
        return sf
