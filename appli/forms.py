from django import forms

class CreerCompteForm(forms.Form):
    identifiant = forms.CharField(label='Identifiant', max_length=100)
    mot_de_passe = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

class LoginForm(forms.Form):
    identifiant = forms.CharField(label='Identifiant', max_length=100)
    mot_de_passe = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
