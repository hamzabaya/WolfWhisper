"""projet_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from appli.views import index_view
from chat.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),  # Set the root URL to the index_view
    path('appli/', include('appli.urls')),  # Include the URLs of the "appli" app
    path('home', home , name ="home"),
    path('<str:room>/', room , name ="room"),
    path('checkview', checkview , name ="checkview"),
    path('send', send , name ="send"),
    path('getMessages/<str:room>/', getMessages , name ="getMessages")
    # Add other URLs if necessary
    # Add other URLs if necessary
]

    