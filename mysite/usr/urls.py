from django.urls import path
from . import views

urlpatterns = [
    path('',views.usr_index,name='usr_index'),
    path('<int:usr_id>',views.usr_get,name='usr_get')
]
