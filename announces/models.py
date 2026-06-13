from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, AbstractUser
# ---------------------------------
# ! Les champs de la table Announce
# ---------------------------------
"""
Titre                                         : Chaine(100)     <ex: Studio moderne a louer>
Type                                          : Chaine(100)     <ex: Chambre, Studio, Appartement, Terrain>
Quartier (liste de selection)                 : Chaine(100)     <ex: [Tamdja, Djeleng]>
Prix (en FCFA)                                : Entier(100)     <ex: 25.000 >
Description                                   : Text()          <ex: Compteur prepayer, Douche interne >
Image_Principale                              : Chaine(100)     <ex: url de l'image >
Date de publication (Remplie automatiquement) : Date()          <ex: datetime.date() >
Disponibilite                                 : Booleen()       <ex: True, False >
Auteur                                        : ForeignKey()    <ex: agent qui poste l'annonce >
"""
# ---------------------------------
# ! Les types de champs
# ---------------------------------
"""
Chaine de caracteres:
    --> CharField(<longeur maximale>)
    --> TextField(<illimite>)
    --> EmailField(<longueur maximale>)
Nombres:
    --> IntegerField(<longeur maximale>)
    --> FloatField(<longueur maximale>)
    --> DecimalField(<longueur maximale>)
Dates et Heures: (a utiliser avec datetime.date())
    --> DateTimeField(auto_now_add=True) (heure et date)
    --> DateField() (uniquement la date)
Logiques:
    --> BooleanField(<longeur maximale>)
    --> FileField()
    --> ImageField()
    --> ForeignKey(<class parente>, on_delete=models.CASCADE)
Autres: 
    --> JSONField
"""
# Create your models here.
class CustomUser(AbstractUser):
    user_phone = models.PositiveIntegerField(null=True, blank=True)


class Announce(models.Model):
    DISTRICT_CHOICES = {
        "Tamdja": "Tamdja",
        "Djeleng": "Djeleng",
        "SOCADA": "SOCADA",
        "Mairie rural": "Mairie rurale",
        "Kamkop": "Kamkop",
        "Banengo": "Banengo",
        "Bafoussam": "Bafoussam",
        "TPO": "TPO",
    }
    title = models.CharField(max_length=100)
    announce_type = models.CharField(max_length=100)
    district = models.CharField(max_length=50, choices=DISTRICT_CHOICES)
    price = models.PositiveIntegerField()
    description = models.TextField()
    main_image = models.ImageField(upload_to='announces/')
    created_date = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
