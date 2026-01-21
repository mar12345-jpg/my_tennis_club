# menbers/urls.py

from django.urls import path
from . import views
    
urlpatterns = [
    # ドメイン直下名のアドレス
   path('', views.main, name='main'),
   path('members/', views.members, name='members'),
   path('test/', views.test, name='test'),
   path('hello/', views.hello, name='hello'),
   path('members/details/<int:id>', views.details, name='details'),
   path('testing/', views.testing, name='testing'),
   path('mypage/', views.mypage, name='mypage'),
]