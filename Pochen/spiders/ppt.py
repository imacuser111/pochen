# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import sys
sys.path.append("/Users/hung-mingchen/Desktop/pochen/Pochen/Pochen")
from items import PochenItem
#from  import items
class PptSpider(scrapy.Spider):
    name = 'ppt'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['http://quotes.toscrape.com/']

    def __init__(self):
        self.h_number = 0
        self.c_number = 0
        # url = start_urls

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.home_page)
            # request_url = requests.get(url)
            # self.home_page(request_url)

    def home_page(self, response):
        soup = BeautifulSoup(response.text,'lxml')
        posts1 = soup.find_all('div', class_= 'row')

        h1 = soup.find('div', class_= 'row.header-box').text
        next_url = soup.select('li.next > a')[0]['href']
        for i in range(20):
            for p in posts1:
                self.h_number = self.h_number + 1
                h1 = p.select('span.text')[0].text
                span = p.select('span')[0].text
                tags = p.select('div.tags')[0].text
                # print(self.h_number, ' : ' , url)
                # request_url = requests.get(
                #     url = category_url,
                #     cookies = {'over18': 'yes'}  # ptt18歲的認證
                # )
                meta = {
                    "homepage" : str(response.url),
                    "h1" : str(h1),
                    "span" : str(sapn),
                    "tags" : str(tags)
                } 
                item = PochenItem()
                item['firstpage'] = meta['firstpage']
                item['username'] = meta['username']
                item['classname'] = meta['classname']
                item['category_pages'] = meta['category_pages']
                item['category_title'] = meta['category_title']
                item['category_url'] = meta['category_url']
                item['a_title'] = meta['a_title']
                item['a_author'] = meta['a_author']
                item['a_date'] = meta['a_date']
                item['note_url'] = meta['note_url']
                item['note'] = meta['note']
                return item
            nextPage_url = 'https://www.ptt.cc/' + next_url
            soup = BeautifulSoup(nextPage_url,'lxml')
            posts1 = soup.find_all('div', class_= 'row')

            

