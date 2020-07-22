# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MySpiderPipeline:
    def process_item(self, item, spider):
        return item

class MaoyanPipeline:
   def process_item(self, item, spider):
        if spider.name != 'maoyan1':
            return item
        m_title = item['m_title']
        m_type = item['m_type']
        m_time = item['m_time']
        # output = f'|{m_title}|\t|{m_type}|\t|{m_time}|\n\n'
        # with open('./maoyanmovie.txt', 'a+', encoding='utf-8') as article:
        #     article.write(output)
        import csv
        f = open('./maoyanmovie.csv','a+',encoding='utf-8', newline='')
        csv_writer = csv.writer(f)
        csv_writer.writerow([m_title, m_type, m_time])
        f.close()
        # with open('./maoyanmovie.csv', 'a+', encoding='utf-8') as article:
        #     article.writerow([m_title, m_type, m_time])
        return item
        
class Maoyan2Pipeline:
   def process_item(self, item, spider):
        if spider.name != 'maoyan2':
            return item
        m_title = item['m_title']
        m_type = item['m_type']
        m_time = item['m_time']
        # output = f'|{m_title}|\t|{m_type}|\t|{m_time}|\n\n'
        # with open('./maoyanmovie2.txt', 'a+', encoding='utf-8') as article:
        #     article.write(output)
        import csv
        f = open('./maoyanmovie2.csv','a+',encoding='utf-8', newline='')
        csv_writer = csv.writer(f)
        csv_writer.writerow([m_title, m_type, m_time])
        f.close()
        return item