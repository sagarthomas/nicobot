from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from rest_framework import generics 
from . import models
from . import serializers

from . forms import CustomUserCreationForm
# Create your views here.

'''class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
'''
class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    
    