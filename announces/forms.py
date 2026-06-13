from django import forms
from announces.models import Announce, CustomUser
from django.contrib.auth.forms import UserCreationForm
# --------------------------------------
# ! Definition de la forme de chaque formulaire
# --------------------------------------

class Add_announce_Form(forms.ModelForm):
    class Meta:
        model = Announce
        fields = ['title', 'announce_type', 'district', 'price', 'description', 'main_image']
        
class User_Form(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'user_phone']
