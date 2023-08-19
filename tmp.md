implementリポジトリとsaasus-sdk-pythonリポジトリがあります  

implementリポジトリからpipでgit経由でsaasus_sdk_pythonというパッケージをインストールして使用したいと考えています。  

saasus-sdk-pythonリポジトリの構成は以下です。

.env
openapi_client(openapi-genaratorで自動生成したもの)
saasus_sdk_python-
                 |-callback-callback.py
                 |-client-client.py
                 |-middleware-middleware.py　　
です。
　　
ここで問題が発生して
implementリポジトリからpipでgit経由でsaasus_sdk_pythonというパッケージをインストールするとリポジトリルートに
2つのパッケージがあるのでエラーになります。  
これを解決する良い方法を教えてください。  
なおopenapi_clientパッケージをsaasus_sdk_python配下に持っていくとエラーになるので持っていきたくないです。