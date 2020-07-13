"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from homepage.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += [
    # path('', RedirectView(url='homepage/',permanent=True)),
    path('',index,name='index'),
    path('homepage/',index,name='index'),
    path('registration/',include('registration.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/',RedirectView.as_view(url='/accounts/login/')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='mysite/templates/login.html')) ,
    path('profile/',include('userprofile.urls')),
    path('post/',include('post.urls')),
    path('usr/',include('usr.urls')),
]
