#-*-coding:utf-8-*-
from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.crawler import CrawlerProcess
import logging
import sys
sys.path.append('..')
import json

JumpScale=10
index=0
class MySpider(scrapy.Spider):
    def __init__(self, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        global index
        index=index+1
        self.startIndex=index
        self.scale=0

        self.log = logging
        self.log.warning("!!!!!!!!This is a warning!!!!!"+str(index))
    
    custom_settings={
        'DOWNLOAD_DELAY':0,
        'RETRY_ENABLED':False
    }

    name = "itjuzi"    

    def start_requests(self):
        yield scrapy.Request('http://www.itjuzi.com/company/'+str(self.startIndex), callback=self.parse)
            
    def parse(self, response):
        item = {}
        item['productName'] = response.xpath('a/text()').extract()
        item['companyName'] = response.xpath('a/@href').extract()
        #item['address'] = response.xpath('text()').extract()        
        self.log.warning('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@') 

        def parse_next(response):
            '''
            if there is a 加入我们, then search the adress around,
            else just pass it.
            ''' 
            item['hireUrl'] = 'ssss' #response.xpath('text()').extract()
            yield json.dump(item, open('newjsonfile.json', 'a'))

        #mainPage = response.xpath('')
        mainPage='http://www.meilishuo.com'
        yield scrapy.Request(mainPage, callback = parse_next)

        #yield item

        self.scale=self.scale+1 
        global JumpScale 
        theindex=self.scale*JumpScale+self.startIndex
        if theindex < 20:  #recursion stop condition
            url = 'http://www.itjuzi.com/company/'+str(theindex)
            yield scrapy.Request(url, callback=self.parse)  
        

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(MySpider)

process.start() # the script will block here until the crawling is finished

# Warming:
#    Coz it's multi spider, but only one output file, if process operate the file at the same time,
# it may occur an error
