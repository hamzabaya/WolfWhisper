# appli/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreerCompteForm, LoginForm
from .models import Utilisateur
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.messages import get_messages

def creer_compte_view(request):
    if request.method == 'POST':
        form = CreerCompteForm(request.POST)
        if form.is_valid():
            identifiant = form.cleaned_data['identifiant']
            mot_de_passe = form.cleaned_data['mot_de_passe']

            # Vérifier si l'utilisateur existe déjà
            if Utilisateur.objects.filter(identifiant=identifiant).exists():
                messages.error(request, 'Identifiant déjà utilisé. Choisissez un autre.')
            else:
                # Créer un nouvel utilisateur
                utilisateur = Utilisateur(identifiant=identifiant, mot_de_passe=make_password(mot_de_passe))
                utilisateur.save()
                messages.success(request, 'Compte créé avec succès. Connectez-vous maintenant.')
                return redirect('sign_in')
        else:
            messages.error(request, 'Form is not valid. Please check the input.')
    else:
        form = CreerCompteForm()

    return render(request, 'html/sign_up.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            identifiant = form.cleaned_data['identifiant']
            mot_de_passe = form.cleaned_data['mot_de_passe']
            try:
                utilisateur = Utilisateur.objects.get(identifiant=identifiant)
                if check_password(mot_de_passe, utilisateur.mot_de_passe):
                    messages.success(request, 'Successfully logged in.')
                    Utilisateur.identifiant = identifiant
                    return redirect('home')
                else:
                    messages.error(request, 'Identifiant ou mot de passe incorrect.')
            except Utilisateur.DoesNotExist:
                messages.error(request, 'Identifiant ou mot de passe incorrect.')

            # Clear existing messages to display only the latest one
            storage = get_messages(request)
            storage.used = True
        else:
            messages.error(request, 'Form is not valid. Please check the input.')
    else:
        form = LoginForm()

    return render(request, 'html/sign_in.html', {'form': form})

def index_view(request):
    return render(request, 'index.html')