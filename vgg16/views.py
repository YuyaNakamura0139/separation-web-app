from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import generic
from .forms import ImageForm
from .models import ImageModel
from project.settings import *
from .cnn import classification
import shutil
import os
import cv2
from PIL import Image


class ImageView(generic.FormView):
    template_name = "index.html"
    form_class = ImageForm

    # postメソッドをオーバーライド
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            # モデルクラス.モデルマネージャ.モデルマネージャのメソッド
            form = ImageForm(request.POST, request.FILES)
            # 前の画像データを消す
            shutil.rmtree(MEDIA_ROOT)
            os.mkdir(MEDIA_ROOT)

            # フォームから受け取った画像データを保存する
            sample = ImageModel()
            sample.img = request.FILES['img']
            sample.save()
            sample_img = sample.img

            # 画像のpathを取得
            path = MEDIA_ROOT + '/images/'
            img_name_arr = os.listdir(path)
            img_name = img_name_arr[0]
            img_path = path + img_name

            # 画像の判定
            img = cv2.imread(img_path)
            result_num = classification(img)
            if result_num > 0.5:
                result = 'ペットボトル'
            else:
                result = '空き缶'
        else:
            form = ImageForm()
            obj = Image.objects.all()

        return render(request, self.template_name, {
            'form': self.form_class, 'result': result, 'sample_img': sample_img
        })
