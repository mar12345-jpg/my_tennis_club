from django.db import models
# データベースの表(テーブル)
# Create your models here.

class Member(models.Model):
    # 列名　＝　データ型クラス(VARCHAR(255))
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True) # 空データOK
    joined_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Book(models.Model):
    # 列名　＝　データ型クラス(VARCHAR(255))
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)