from django.urls import path,include
from . import views
from django.contrib import admin 

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name = 'signup'),
    path('', views.UserListView.as_view())
    ] 
