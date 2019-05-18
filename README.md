# 專題實作後端 
## (尚未解決需思考的問題)
> 爬蟲的精確度以及資料過濾
> 資料庫欄位設定以及資料表的連接
> 主鍵的設定
> json的顯示方式
> 搜尋的功能
> CRUD,GET,POST(是否要直接使用rest framework)
###### tags: `專題`




## 使用環境前置作業
參考：https://github.com/twtrubiks/django-transactions-tutorial
> install django 
> install PyMySQL
> install mysqlclient

## 資料庫連接出錯排除

匯入語法參考網址
>https://www.itread01.com/lfepy.html

資料匯入語法:
![](https://i.imgur.com/Y8XHchy.png)
![](https://i.imgur.com/XnFRmUE.png)

1. > ### 錯誤訊息 **(Error Code 1209)**
```
Error Code: 1290. The MySQL server is running with the --secure-file-priv option so it cannot execute this statement
```

可以透過my.ini進行修改(參考網站內的修改)

解決方式參考:https://ithelp.ithome.com.tw/articles/10197804?sc=rss.qu

# 


2. > ### 錯誤訊息 **(Error Code 1261)**

![](https://i.imgur.com/lPFyLZS.png)

解決方式:要注意最後一行後還有沒有空白!!

# 

3. > ### 錯誤訊息 **(Error Code 1062)**

![](https://i.imgur.com/eSGun8l.png)

主鍵有相同，這個部分還要想辦法改進

4. > ### 錯誤訊息 **(Error Code 1262)**
![](https://i.imgur.com/PyKaU23.png)

可能資料裡有多出的逗號，要在資料裡檢查有沒有多出並刪除

## 建立超級使用者 
```
python manage.py createsuperuser
```

## ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑2019/05/14進度 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

## 修改顯示資訊

透過下列方式，可以修改要顯示的範圍(要對應到資料庫)
![](https://i.imgur.com/J5K18E7.png)
## 

## 序列化

參考網站:
https://www.cnblogs.com/iiiiiher/articles/9170572.html

https://docs.djangoproject.com/en/2.2/ref/contrib/gis/serializers/

http://www.liujiangblog.com/course/django/171

> ### 第一種
views:
![](https://i.imgur.com/AvOJcvc.png)

自己創一個serializers:
![](https://i.imgur.com/ZMHiL4P.png)

結果
![](https://i.imgur.com/tFP1kUU.png)


> ### 第二種
views:
![](https://i.imgur.com/MWUno4T.png)

template/index.html:
![](https://i.imgur.com/15poMdS.png)

![](https://i.imgur.com/L590TWD.png)



## 使用restframework(在分支restframework下)

### ---Serializers.py
這裡的HyperlinkedModelSerializer，是設定物件關聯性
>參考資料:https://www.atjiang.com/django-rest-tut5-relationships-and-hyperlinked-apis/

![](https://i.imgur.com/ca08rbB.png)

### ---Views.py
> 使用ViewSet來設定

![](https://i.imgur.com/NMboaaA.png)
![](https://i.imgur.com/vuLYnJd.png)

### ---Viewset.py
> 為了分類，建造一個viewset，將上面的動作做在viewset中

![](https://i.imgur.com/4sS3CBV.png)

> 然後設定Urls




### ---Urls.py
> 利用Router，我們可以快速設定網址
> 定義一個router，他的網址位置是data，網頁內容是DataViewSet

```
router = DefaultRouter()
router.register(r'data',DataViewSet)
```

![](https://i.imgur.com/7ipjMPZ.png)


![](https://i.imgur.com/t4dQxVh.png)

## 授權

在viewset中，使用IsAuthenticated
![](https://i.imgur.com/2hdIxv1.png)

引入登入頁面URL
![](https://i.imgur.com/UTuaqpq.png)

## 解析 Parsers

> 參考網站:http://www.django-rest-framework.org/api-guide/parsers/#parsersr

讓你的Content-Type只接受某種類型
通常如果沒有特別去設定 ，一般預設是使用 application / x-www-form-urlencode


![](https://i.imgur.com/m4CmFsx.png)

全域設定方式
```
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}
```
![](https://i.imgur.com/tJLyTbm.png)

區域設定(設定在自己想要的view上)

![](https://i.imgur.com/JbbP5WN.png)


## 自行設定get , post 所需的授權

> ### get 新增下列內容
> 1.get_permissions
> 2.status
> 3.def list
> 4.context,many

![](https://i.imgur.com/4WPioYb.png)



#### 1.get_permisssions

繼承下面方法，會透過return來回傳permission
![](https://i.imgur.com/hWKMTke.png)

所以可以透過下面修改，讓使用者要進行(create的時候，要認證)
![](https://i.imgur.com/WE7DvQ7.png)


#### 實際get方法(list)

繼承list方法
![](https://i.imgur.com/5A2LD6c.png)

--mixins.py
![](https://i.imgur.com/7QKSe1i.png)

#### status

參考網站:https://www.django-rest-framework.org/api-guide/status-codes/

> 用來定義http，增加可讀性

![](https://i.imgur.com/MCpogzx.png)

#### context / many

> 因為我們使用的是HyperlinkedModelSerializer，所以需要回傳一個request

![](https://i.imgur.com/iM7GWPs.png)

> 然後加上request的傳送

![](https://i.imgur.com/Z9TRK2v.png)

> 而many則是敘述該物件是多個還是單個

![](https://i.imgur.com/4836Uf6.png)

## 

> ### post
> 預設@permission_classes都會去呼叫get_permission這個函式，所以我們可以透過複寫他，來操作權限得使用


![](https://i.imgur.com/zmIHfuD.png)

## 連接css

![](https://i.imgur.com/rIH8jjZ.png)

![](https://i.imgur.com/3VMtYM0.png)

## detail的使用

> 新增一個detail方法，去分配每個id的url

--view.py配置
![](https://i.imgur.com/T2lcXCt.png)

--url.py配置
![](https://i.imgur.com/reNZm9p.png)

--detail.html配置
![](https://i.imgur.com/NbNC3eS.png)

## 將主頁和小頁分開
![](https://i.imgur.com/JAN1SLC.png)


## Raw SQL 

因為rest framework改版後，捨棄@list_route和@detail_route
改使用action，下面是action詳細介紹
![](https://i.imgur.com/hcflJcD.png)

```
@action(methods=[GET or POST], detail = True)
```
而我們要使用Raw SQL，所以先在models下建立函式
![](https://i.imgur.com/s7Abc5r.png)

然後再在viewset下新增一個方法，被action繼承

![](https://i.imgur.com/XW4Mwlg.png)

結果
![](https://i.imgur.com/Ul5iTFU.png)
