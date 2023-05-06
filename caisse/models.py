from django.db import models


class Caisse(models.Model):
    reference = models.CharField(max_length=100)
    libele = models.TextField()
    montant = models.DecimalField(max_digits=15, decimal_places=2,default=0)
    date = models.DateField()
    typeO=models.CharField(max_length=100)
    def __str__(self):
        return self.reference
    
    
    
class Solde(models.Model):
    soldeI = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    
    def __str__(self):
        return f"Solde Initial: {self.soldeI}"
    

    