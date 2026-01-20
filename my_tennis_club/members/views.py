# 今の書き方　短いよ

from django.shortcuts import render

def members(request):
    return render(request, 'myfirst.html')


# 下記は昔の書き方

# from django.shortcuts import render

# from django.http import HttpResponse
# from django.template import loader

# # Create your views here.あなたのビューをここに書いて
# # パスと連動した関数を書く

# def members(request):
#    # htmlファイルを探す
#    template = loader.get_template('myfirst.html')
#    # htmlファイルをデータ化して返信する
#    return HttpResponse(template.render())