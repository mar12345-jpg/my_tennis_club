from django.contrib import admin
from .models import Member
    
# Register your models here.
# memberテーブルを管理者サイトに登録
admin.site.register(Member)