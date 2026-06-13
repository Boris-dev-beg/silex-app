from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User
from announces.models import Announce, CustomUser # ? permet d'importer le model Announce depuis le fichier models.py de l'application announces

# ! Mes infos de connexion à l'interface d'administration de Django: 
# ? username: mangwaboris 
# ? password: brillant12
# ? email: borisweteneyi1@gmail.com
# ? pour accéder à l'interface d'administration de Django, il faut se rendre à l'URL suivante: http://localhost:8000/admin/ et entrer les informations de connexion ci-dessus.


# ! Register your models here.
@admin.register(Announce) # ? permet de register le model Announce dans l'interface d'administration de Django
class AnnounceAdmin(admin.ModelAdmin): # ? permet de personnaliser l'affichage du model Announce dans l'interface d'administration de Django
    # Permet d'afficher les champs title, announce_type, district, price et available dans la liste des annonces
    list_display = ("title", "announce_type", "district", "price", "available", "main_image")
    # Permet de filtrer les annonces par type, district et disponibilité
    list_filter = ("announce_type", "district", "available")
    # Permet de rechercher des annonces par titre et description
    search_fields = ("title", "description")

@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    # 1. Pour l'affichage des colonnes
    list_display = ('username', 'email', 'user_phone', 'is_staff', 'is_active')
    # 2. Pour l'affichage dans la page de modification d'un utilisateur
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Informations personnalisees', {'fields': ('user_phone',)}),
    )
    # 3. Pour l'affichage lors de la creation d'un utilisateur depuis l'admin
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Informations personnalisees', {'fields': ('user_phone',)}),
    )
    # Permet de rechercher des annonces par titre et description
    search_fields = ("title", "description")

# admin.site.register(CustomUser, BaseUserAdmin)

# # ? Permet une description admin en ligne pour le model CustomUSer
# class CustomUserAdmin(admin.StackedInline):
#     model = CustomUser
#     can_delete = False
#     verbose_name_plural = 'customuser'

# # ? Pour definir le nouveau model Admin
# class UserAdmin(BaseUserAdmin):
#     inlines = [CustomUserAdmin]

# # ? Pour re-enregistrer UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
