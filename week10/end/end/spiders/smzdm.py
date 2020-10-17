import scrapy
from scrapy.selector import Selector
from end.items import EndItem
class SmzdmSpider(scrapy.Spider):
    name = 'smzdm'
    allowed_domains = ['smzdm.com']
    start_urls = ['https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/']

    info = None
    
    def start_requests(self):
        url = 'https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        ul = Selector(response=response).xpath('//*[@id="feed-main-list"]/li[position()<11]')
        for li in ul:
            item = EndItem()
            link = li.xpath('./div/div[2]/h5/a/@href')[0].get()
            title = li.xpath('./div/div[2]/h5/a/text()')[0].get()
            item['phone'] = title
            item['alink'] = link
            item['user_comment'] = []
            yield scrapy.Request(
                url=link, 
                meta={'item': item}, 
                callback=self.parse2)


    def parse2(self, response):
        item = response.meta['item']
        ul = Selector(response=response).xpath('//*[@id="commentTabBlockNew"]/ul[1]/li')
        alink = Selector(response=response).xpath('(//*[@class="pageCurrent"])[2]/../following-sibling::li[1]/a/@href').get()
        # alink = Selector(response=response).xpath('(//*[@class="pagedown"])[2]/preceding-sibling::li').getall()
        print(alink)
        
        for li in ul:
            user = li.xpath('./div[2]/div[1]/a/span/text()')[0].get()
            comment = li.xpath('./div[2]/div[@class="comment_conWrap"]/div[1]/p/span/text()').get()
            # 当出现图片表情时会多出img标签，comment就会多出空白内容。
            # 因此将comment列表直接拼接
            comment = ''.join(comment).strip()
            item['user_comment'].append((user, comment))
        if alink:
            yield scrapy.Request(url=alink, meta={'item': item}, callback=self.parse2)
        else:
            yield item




    