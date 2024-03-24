# appli/urls.py

from django.urls import path
from .views import creer_compte_view, login_view, index_view

urlpatterns = [
    path('', index_view, name='index'),  # Set the root URL to the index_view
    path('sign_up/', creer_compte_view, name='sign_up'),
    path('sign_in/', login_view, name='sign_in'),
]
