from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
# appli/models.py

from django.db import models

class Utilisateur(models.Model):
    identifiant = models.CharField(max_length=255, unique=True)
    mot_de_passe = models.CharField(max_length=255)

    def __str__(self):
        return self.identifiant