from django import forms
from .models import ImageModel


# django.forms.ModelFormを継承したクラスを作成する
# 中にMetaクラスを作成して、どのModelに対するフォームなのか定義を記載する
class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ('img',)
