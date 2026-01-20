from django.db import models
# データベースの表(テーブル)
# Create your models here.

class Member(models.Model):
   # 列名　＝　データ型クラス(VARCHAR(255))
   firstname = models.CharField(max_length=255)
   lastname = models.CharField(max_length=255)
