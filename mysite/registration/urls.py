from django.urls import path
from . import views

from django.urls import include, path

urlpatterns = [
    path('', views.signup,name ='signup'),
    path('logout/',views.logout_view,name='logout_view'),
    # path('',views.index,name = 'index'),
]
