# 毕业总结

时过境迁，12周走过了，从一开始的激动到最后的淡然表明了这又是一段成长！
因最后一段时间学的不太行，毕业项目没用上celery等一些工具去完善项目，从而只是简单的爬取数据后处理部分没见过的异常(如：SNOWNLP 中sentiments 出现division by zero。hah)进行展示数据。

## 经验与遇到的问题
1. scrapy Selector XPath 获取的内容，可以用get、getall提取内容，比extrace 更新更方便。
2. 在写parse2函数并想进行递归调动时总是发现不成功，以为是不能递归调用的锅qaq，然后改来改去，最终发现是遵循robots.txt导致的不能爬取。（因为一般用的--nolog因此没发现qaq）。
3. 在写parse2的时最后的yield item 前没加else，导致递归调用时存了2W行评论到数据库中，修改后只有2000条左右hah。
4. 写django时index app时总是寻找根目录的static(只好把文件放根目录qaq)...而templates还去用另一个app里的同名.html...只好把另一个app在settings里取消install...(现在惊醒：应该用appname/xxx.html！！！)

## 最后
hah，虽然这期过去了，学到了很多很多很多，不过应用方面有点少qaq，好在给老学员同步2.0版本，以现在的自己再重新来一遍稳赚不亏！感谢极客时间。
