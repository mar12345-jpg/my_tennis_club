# members/forms.py(手作り)
# HTMLフォーム構成要素と入力データ格納クラス

from django import forms
from .models import Member

# Memberモデルと直結したフォーム
class MemberModelForm(forms.ModelForm):
    class Meta:
        model = Member # 紐付けるモデルを指定
        fields = ['firstname', 'lastname', 'phone', 'joined_date'] # 使う項目を指定