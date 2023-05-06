from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_grh = models.BooleanField(default=False)
    is_gstock = models.BooleanField(default=False)
    is_comptable = models.BooleanField(default=False)
    is_anonimous = models.BooleanField(default=True)
    