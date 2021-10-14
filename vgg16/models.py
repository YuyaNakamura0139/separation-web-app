from django.db import models

# Create your models here.
from django.db import models


class ImageModel(models.Model):
    # アップロード配下のimagesディレクトリにアップロードしたファイルを保存
    img = models.ImageField(upload_to='images/', verbose_name='画像')
