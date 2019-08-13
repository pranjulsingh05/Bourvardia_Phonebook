"""Phonebook_Project URL Configuration

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

from Phonebook_App import login, phone_verification, profile, views

#from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^swagger$', schema_view),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # UserLogin_Api
    url(r'^userlogin$', login.UsersLogin.as_view(), name="User Login"),

    # UserHomeView_Api
    url(r'^homepage$', profile.HomeView.as_view(), name="Home page of user"),

    # UserDetailView_Api
    url(r'^userview$', profile.UsersView.as_view(), name="User Detail View"),

    # UserSearchedView_Api
    url(r'^searcheduserview$', views.SearchedUsersView.as_view(), name="Search User Detail"),

    # UserUpdateView_Api
    # url(r'^userupdateview/(?P<pk>[0-9]+)$', profile.usersupdateview),

    # ManagerSearch_Api
    url(r'^usersearch$', views.ManagerSearch.as_view(), name="User Search-->Manager"),

    # Search_Api
    url(r'^search$', views.Search.as_view(), name="Search"),

    # Viewrarchi_Api
    url(r'^userhierarchy$', views.ViewHierarchy.as_view(), name="ViewHierarchy"),

    # Hierarchy_Api
    url(r'^newhierarchy$', views.UserHierarchy.as_view(), name="UserHierarchy"),

    # SendOpt_Api
    url(r'^sendotp$', phone_verification.sendotp, name="Send-Opt"),

    # VerifyOpt_Api
    url(r'^verifyotp$', phone_verification.verify, name="Verify-Opt"),

    # url(r'^status$', phone_verification.status),

    # AddManager_Api
    url(r'^addmanager/(?P<pk>[0-9]+)$', profile.AddManager.as_view(), name="Add-Manager"),

    # LaguageSkillResponse_Api
    url(r'^responseskills$', profile.SkillResponse.as_view(), name="Get all Skill"),

    # DesignationResponse_Api
    url(r'^responsedesignation$', profile.DesignationResponse.as_view(), name="Get All Designation"),

    # Logout_Api
    url(r'^userlogout$', login.Logout.as_view(), name="User-Logout"),

    # UserUpdateView_Api
    url(r'^userupdateview/(?P<pk>[0-9]+)$', profile.UserUpdateView.as_view(), name="User Update Detail"),

]
