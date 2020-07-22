# -*- coding: utf-8 -*-
import scrapy
# from bs4 import BeautifulSoup
from my_spider.items import MaoyanItem
from scrapy.selector import Selector


class Maoyan2Spider(scrapy.Spider):
    name = 'maoyan2'
    allowed_domains = ['maoyan.com']
    # 起始URL列表
    start_urls = ['https://maoyan.com/films?showType=3']

#   注释默认的parse函数
#   def parse(self, response):
#        pass


    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)
        # url 请求访问的网址
        # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
        # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数
    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')[:11]
        for movie in movies:
            item = MaoyanItem()
            m_title = movie.xpath('./div[1]/span[1]/text()')
            m_type = movie.xpath('./div[2]/text()')[-1]
            m_time = movie.xpath('./div[4]/text()')[-1]
            print(m_title.extract_first().strip())
            print(m_type.extract().strip())
            print(m_time.extract().strip())
            item['m_title'] = m_title.extract_first().strip()
            item['m_type'] = m_type.extract().strip()
            item['m_time'] = m_time.extract().strip()
            yield item