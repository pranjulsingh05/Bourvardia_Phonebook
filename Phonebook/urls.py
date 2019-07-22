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
from django.contrib import admin
from django.urls import path
from Phonebook_backend import views, login, profile, phone_verification
from django.conf.urls import url, include
#from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
#schema_view = get_swagger_view(title='PhoneBook API')

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^swagger$', schema_view),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^userlogin$', login.Users_Login.as_view()),
    url(r'^homepage$', profile.Home_View.as_view()),
    url(r'^userview$', profile.Users_View.as_view()),
    url(r'^searcheduserview$', views.Searched_Users_View.as_view()),
    url(r'^userupdateview/(?P<pk>[0-9]+)$', profile.users_updateview),
    url(r'^usersearch$', views.Manager_Search.as_view()),
    url(r'^search$', views.Search.as_view()),
    url(r'^userhierarchy$', views.View_Hierarchy.as_view()),
    url(r'^userlogout$', login.User_Logout),
    # url(r'^hrupdateview/(?P<pk>[0-9]+)$', profile.hr_updateview),
    url(r'^sendotp$', phone_verification.sendotp),
    url(r'^verifyotp$', phone_verification.verify),
    # url(r'^status$', phone_verification.status),
    url(r'^addmanager/(?P<pk>[0-9]+)$', profile.add_manager),
    url(r'^newhierarchy$', views.User_Hierarchy.as_view()),
    url(r'^responseskills$', profile.skill_response),
    url(r'^responsedesignation$', profile.designation_response),
]
