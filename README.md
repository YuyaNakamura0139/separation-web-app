# ゴミの分別アプリ(Garbage Separation App)  

![garbage-separation-app](https://user-images.githubusercontent.com/84562508/138389413-9358c625-2b11-473f-a63b-5f1de29b06da.png)   


# 概要

ゴミの中でもペットボトルと空き缶に焦点をあてました。  

画像をアップロードするとその画像がペットボトルなのか空き缶なのかAIが判断し結果を返してくれます。  

CNNモデルを自作し、学習データは自分で写真を撮って収集し、足りない分はスクレイピングして収集しました。
  
[https://garbage-separation-app.ml/](https://garbage-separation-app.ml/)  
 
# 使用技術
 
* Python 3.7.10
* Django 3.2.8
* Nginx
* Gunicorn
* AWS
  * EC2
  * Routo53
  * VPC
 
# AWS構成図
  
![AWS](https://user-images.githubusercontent.com/84562508/138400766-8ae237e8-bef4-4a5f-b28c-a5912b5ee295.png)
  
取得した独自ドメインはRoute53でElasticIPと紐付けしました。
WebサーバーにはNginx、AppサーバーにはGunicornを用いました。
静的リクエストの場合はNginxが処理し、動的リクエストの場合はNginxがGunicornに処理を委譲することでサーバーの負荷を分散しています。  
https化も行いましたので安全にWebページをご覧になれます。

# Author
[**YuyaNakamura**](https://twitter.com/yuya_0139)
