from django.contrib import admin
from django.urls import path, include
from .views import calculation, start
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('form/', calculation),
    path("start/", start)
]