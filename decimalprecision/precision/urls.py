from django.urls import path
from . import views

urlpatterns = [
    path('', views.cde),
    path('retri', views.retrieve),
]
