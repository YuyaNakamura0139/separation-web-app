from django.urls import path

from . import views

app_name = 'vgg16'
urlpatterns = [
    path('', views.ImageView.as_view(), name="index"),  # as_view()はクラスベースビューをビュー関数化する
]
