"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from announces import views # ? permet d'importer les vues de l'application announces pour pouvoir les utiliser dans les URL patterns ci-dessous

urlpatterns = [
    path('admin/', admin.site.urls),
    # ! URLs de l'authentification
    path('auth/registration/', views.register, name='register'),
    path('auth/login/', auth_views.LoginView.as_view(template_name='authentication/login.html'), name='login'),
    # path('auth/login/', views.login, name='login'),
    path('auth/logout/', auth_views.LogoutView.as_view(), name='logout'),
    # ! URLs de la page d'accueil
    path('', views.index, name='index'),
    # ! URLs de la page d'annonces
    path('announces/', views.announces, name='announces'),
    # ! URLs du CRUD des annonces
    path('/announce/<int:id>', views.details, name='details'),
    path('announce/<int:id>/edit', views.edit_announce, name='edit'),
    path('announce/<int:id>/delete', views.delete_announce, name='delete'),
    path('/announce/add', views.add_announce, name='add'),
    # ! URLs du dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/announces/', views.announces_dashboard, name='announces_dashboard'),
]

# ? Pour servir les fichiers medias pendant le developpement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)