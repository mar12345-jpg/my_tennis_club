# 昔の書き方

from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.shortcuts import render

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

def testing(request):
   template = loader.get_template('template.html')
   context = {
            # {{キー名}}
          'firstname': 'Linus',
          'price': 1200,
          'greeting': 1,
          'emptytestobject': [],
          'fruits': ['Apple', 'Banana', 'Cherry', 'Oranges', 'Kiwi'],
    }
   return HttpResponse(template.render(context, request))

   # # htmlファイルを探す
   # template = loader.get_template('myfirst.html')
   # # htmlファイルをデータ化して返信する
   # return HttpResponse(template.render())

def test(request):
    return HttpResponse("<h2>test テストです！</h2>")

def hello(request):
    ans = 12*2
    str = f"答え = {ans}"
    return HttpResponse(str)

def mypage(request):
    template = loader.get_template('mypage.html')
    context = {
        'username': 'Taro',
        'age': 25,
        'message': 'ようこそ、マイページへ！',
    }
    return HttpResponse(template.render(context, request))

def get_post(request):
    # message という変数を初期化（最初は何も入れない）
    message = None

    # ブラウザから送られてきた HTTP メソッドを判別
    if request.method == "GET":
        # GET のときに行う処理
        # ページを開いたとき（リンクをクリックしたとき）など
        message = "GET"

    elif request.method == "POST":
        # POST のときに行う処理
        # フォームを送信したときなど
        message = "POST"

    # テンプレートに渡すデータを辞書でまとめる
    context = {'message': message}

    # get_post.html を表示し、context の内容をテンプレートに渡す
    return render(request, 'get_post.html', context)

def nameform(request):
    display_name = None
    
    # フォームに入力されたデータの取得
    if request.method == 'POST':
        display_name = request.POST.get('your_name')

    context = {
        'display_name': display_name,
    }
    
    return render(request, 'nameform.html', context)


# # 今の書き方　テンプレート読み込み → レンダリング → レスポンス をまとめて実行
# from django.http import HttpResponse
# from django.shortcuts import render

# def members(request):
#     return render(request, 'myfirst.html')


