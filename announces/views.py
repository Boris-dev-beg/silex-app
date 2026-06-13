from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from announces.models import Announce, CustomUser
from .forms import Add_announce_Form, User_Form

from datetime import datetime

# ! -----------------
# ! CRUD OPERATION
# ! -----------------
"""
    -> from <app>.models import <model>
# ? CREATE :
    -> <instance> = <model>(<champ1>=<val1>, ..., <champn>=<valn>)
    -> <instance>.save() # ? il ne va enregistrer que lorsque cette methode est appelee
# ? READ :
    -> <instance>.objects # ! impossible
    -> <All_entries> = <model>.objects.all() # ? Recupere tous les donnees
    -> <All_entries> = <model>.objects.all()[<debut>:<fin>:<step>] # ? Recupere tous les donnees avec une limit
    -> <Specified_entries> = <model>.objects.get(<condition>) # ? Recupere la donnee qui verifie la <condition>
    -> <Specified_entries> = <model>.objects.filter(<condition>) # ? Recupere tous les donnees qui verifie la <condition>
    -> <Specified_entries_Whitout_Others> = <model>.objects.exclude(<condition_exclusion>) # ? Recupere tous les donnees et exclue ceux qui ne respectent pas la <condition_exculsion> 
    -> <Specified_entries_Whitout_Others> = <model>.objects.filter(<condition>).(<condition_exclusion>) # ? Recupere tous les donnees qui verifie la <condition> et exclue ceux qui ne respectent pas la <condition_exculsion> 
# ? UPDATE :
    -> <model>.objects.update(<field>=<val>) # ? Mets toutes les donnees a jours
    -> <model>.objects.filter(<condition>).update(<field1>=<val1>, <fieldn>=<valn>) # ? Mets certaines donnees a jours
    -> <instance_var> = get_object_or_404(<Model>, id=id)
        form = <Model_Form>(request.POST, instance=<instance_var>)
        form.save()
# ? DELETE :
    -> <model>.delete() # ? Supprime l'objet
    -> <model>.objects.all().delete() # ? Supprime tous les entrees de l'objets

<condition> => <field_name>_<elt_to_chech>=<val_to_compare>, pk(primary_key) = <value>
                            <elt_to_check> :
                                -> _year, _date, etc
                                -> _startswith, _endswith, istartswith(get with the case sentise), iendswith(get with the case sensitive)
                                -> gt, lt, _gte(greater than egal to), _lte(lower than egal to), _exact(egal), _contains(LIKE '% %')
"""

# Create your views here.
def index(request):
    announces = Announce.objects.all()[:3] # ? Permet de récupérer toutes les annonces de la base de données et de les stocker dans la variable announces
    
    return render(request, 'announce/index.html', {'announces': announces})

def announces(request):
    announces = Announce.objects.all()
    return render(request, 'announce/announces.html', {'announces': announces})

def register(request):
    form = ""
    if request.method == "POST":
        form = User_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(f'form Errors: {form.errors.as_data()}')

    return render(request,'authentication/register.html', {"form": form})

def details(request, id):
    announce = Announce.objects.get(id__exact=id)
    return render(request, 'announce/announce_details.html', {'announce': announce})

@login_required
def add_announce(request):
    form = ""
    if request.method == "POST":
        # ? Create a form instance with the datas whose came from the form
        form = Add_announce_Form(request.POST, request.FILES)
        # ? Check if wheter it's valid
        if form.is_valid():
            # ? Save it but not send
            announce = form.save(commit=False)
            # ? Add author 
            announce.author = request.user
            # ? Send it into the database
            announce.save()
            # ? Redirect to a new URL
            messages.success(request, "The form has been successuflly uploaded")
            return redirect('dashboard')
        else:
            messages.error(request, f"Failed to upload the form, please check the errors below, {form.errors}")

    return render(request, 'announce/add_announce.html', {"form": form})

@login_required
def edit_announce(request, id):
    form = ""
    announce = Announce.objects.get(id__exact=id)
    if announce.author != request.user:
        return 
    
    # ! Modification de l'annonce
    announce_Form = get_object_or_404(Announce, id=id)
    if request.method == "POST":
        # ? Create a form instance with the datas whose came from the form
        form = Add_announce_Form(request.POST, request.FILES, instance=announce_Form)
        # ? Check if wheter it's valid
        if form.is_valid():
            form.save()
            # ? Redirect to a new URL
            messages.success(request, "The form has been successuflly uploaded")
            return redirect('dashboard')
        else:
            messages.error(request, f"Failed to upload the form, please check the errors below, {form.errors}")

    return render(request, 'announce/edit_announce.html', {"announce": announce, "form": form})

@login_required
def delete_announce(request, id):
    announce = Announce.objects.get(id__exact=id)
    # ! Suppression
    announce.delete()
    # ! Redirection vers le dashboard
    announces = Announce.objects.filter(author__exact=request.user)[:3]
    
    return render(request, 'dashboard/dashboard.html', {"announces": announces})

@login_required
def dashboard(request):
    announces = Announce.objects.filter(author__exact=request.user)[:3]
    return render(request, 'dashboard/dashboard.html', {"announces": announces})

@login_required
def announces_dashboard(request):
    announces = Announce.objects.filter(author__exact=request.user)
    return render(request, 'dashboard/announces_dashboard.html', {"announces": announces})
