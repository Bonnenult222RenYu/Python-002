# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from my_spider.items import MaoyanItem


class MaoyanSpider(scrapy.Spider):
    # 定义爬虫名称
    name = 'maoyan1'
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
        soup = BeautifulSoup(response.text, 'html.parser')
        title_list = soup.find_all('div', attrs={'class': 'movie-hover-info'})
        #for i in range(len(title_list)):
        # 在Python中应该这样写
        for i in title_list[:11]:
            # 在items.py定义
            item = MaoyanItem()
            m_list =i.find_all('div', attrs={'class': 'movie-hover-title'})
            m_title = m_list[0].find('span').text.replace(' ', '').replace('\n', '')
            m_type = m_list[1].text.replace(' ', '').replace('\n', '')
            m_time = m_list[3].text.replace(' ', '').replace('\n', '')

            item['m_title'] = m_title
            item['m_type'] = m_type
            item['m_time'] = m_time
            
            yield item

    # # 解析具体页面
    # def parse2(self, response):
    #     item = response.meta['item']
    #     soup = BeautifulSoup(response.text, 'html.parser')
    #     # content = soup.find('div', attrs={'class': 'related-info'}).get_text().replace(' ', '').replace('\n', '')
    #     content = soup.find('div', attrs={'class': 'related-info'}).get_text().strip()
    #     item['content'] = content
    #     yield item

