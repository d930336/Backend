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

