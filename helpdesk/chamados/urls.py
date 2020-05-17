from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', inicial, name='inicio'),
    path('detalhes/<int:id_chamado>', detalhes, name='detalhes'),
]