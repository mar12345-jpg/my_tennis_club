# 昔の書き方

from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.あなたのビューをここに書いて
# パスと連動した関数を書く

def members(request):
   mymembers = Member.objects.all().values()
   template = loader.get_template('all_members.html')
   # HTMLに渡す辞書データ
   context = {
     'mymembers': mymembers,
   }
   return HttpResponse(template.render(context, request))

# 個人データを表示
def details(request, id):
   # idで検索して１件のレコードを取得
   mymember = Member.objects.get(id=id)
   template = loader.get_template('details.html')
   context = {
      'mymember': mymember,
   }
   return HttpResponse(template.render(context, request))

def main(request):
   template = loader.get_template('main.html')
   return HttpResponse(template.render())

   # # htmlファイルを探す
   # template = loader.get_template('myfirst.html')
   # # htmlファイルをデータ化して返信する
   # return HttpResponse(template.render())

def test(request):
    return HttpResponse("<h2>test テストです！</h2>")

def hello(request):
    ans = 12*2
    str = f"答え = {ans}"
    return HttpResponse("<h2>test テストです！</h2>")


# # 今の書き方　テンプレート読み込み → レンダリング → レスポンス をまとめて実行
# from django.http import HttpResponse
# from django.shortcuts import render

# def members(request):
#     return render(request, 'myfirst.html')



