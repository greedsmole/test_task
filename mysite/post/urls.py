from django.urls import path
from . import views

from django.urls import include, path

urlpatterns = [
    path('new',views.newpost,name='newpost'),
    path('<int:post_id>/update/',views.updatepost,name='updatepost')
    # path('update/<int:post_id>',views.updatepost,name='updatepost'),
    # path('update/submit',views.submit,name='updatepost')
    # path('',views.index,name = 'index'),
]
