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
    path('members/mypage/', views.mypage, name='mypage'),
    # /members/get_post/ にアクセスしたとき get_post 関数を呼び出す
    path('get_post/', views.get_post, name='get_post'),
]