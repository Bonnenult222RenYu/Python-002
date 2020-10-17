# 作业

## 爬虫:end

爬取[24h前10手机](https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/)的评论存入数据库。

修改[/end/end/settings.py](https://github.com/Bonnenult222RenYu/Python-002/blob/master/week10/end/end/settings.py)中DATABASES连接信息并在/end/end路径下执行`scrapy crawl smzdm`即可存入值定的数据库。

[comments.sql](https://github.com/Bonnenult222RenYu/Python-002/blob/master/week10/comments.sql)是从数据库转存出来的爬取结果示例。

## Django:end_django

在爬取数据已存在时，修改[/end_django/end_django/settings.py](https://github.com/Bonnenult222RenYu/Python-002/blob/master/week10/end_django/end_django/settings.py)中数据库连接信息并在/end_django路径下执行`python manage.py runserver 0.0.0.0:8080`即可在浏览器的[127.0.0.1:8080/end/](http://127.0.0.1:8080/end/)查看展示结果。

我的在线示例演示结果：[end](https://hello222world.top/end/)

