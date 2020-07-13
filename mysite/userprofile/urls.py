from django.urls import path
from . import views

from django.urls import include, path

urlpatterns = [
    path('',views.userprofile,name='userprofile')
]
