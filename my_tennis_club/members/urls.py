# menbers/urls.py

from django.urls import path
from . import views
    
urlpatterns = [
   path('members/', views.members, name='members'),
   path('test/', views.members, name='test'),
   path('hello/', views.members, name='hello'),
]