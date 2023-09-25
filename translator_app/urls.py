from django.contrib import admin
from django.urls import path
from .views import translatorView

urlpatterns = [
    path('', translatorView, name="translator_url"),
]