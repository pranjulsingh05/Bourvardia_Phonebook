"""Phonebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from Phonebook_backend import login, phone_verification, profile, views

#from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^swagger$', schema_view),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^userlogin$', login.UsersLogin.as_view()),
    url(r'^homepage$', profile.HomeView.as_view()),
    url(r'^userview$', profile.UsersView.as_view()),
    url(r'^searcheduserview$', views.SearchedUsersView.as_view()),
    url(r'^userupdateview/(?P<pk>[0-9]+)$', profile.usersupdateview),
    url(r'^usersearch$', views.ManagerSearch.as_view()),
    url(r'^search$', views.Search.as_view()),
    url(r'^userhierarchy$', views.ViewHierarchy.as_view()),
    url(r'^userlogout$', login.Logout.as_view()),
    url(r'^sendotp$', phone_verification.sendotp),
    url(r'^verifyotp$', phone_verification.verify),
    # url(r'^status$', phone_verification.status),
    url(r'^addmanager/(?P<pk>[0-9]+)$', profile.addmanager),
    url(r'^newhierarchy$', views.UserHierarchy.as_view()),
    url(r'^responseskills$', profile.skillresponse),
    url(r'^responsedesignation$', profile.designationresponse),
]
