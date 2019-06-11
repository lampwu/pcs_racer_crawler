import scrapy
from pcs_racer.items import pcsRacerItem

class PcsSpider(scrapy.Spider):
    name = "pcsrace"
    start_urls = [
        'https://www.procyclingstats.com/rider/chad-haga'
    ]

    def parse(self, response):
        for race in response.css('tbody tr'):
            item = pcsRacerItem() 
            item['riderName'] = response.css('div.content div.entry h1::text').get()
            item['teamName'] = response.css('div.content div.entry h1 span::text')[1].getall()
            item['country'] = response.css('div.content div.entry span::attr(class)')[0].getall()
            item['riderCountryFlag'] = response.css('div.content div.entry span::attr(class)')[0].getall()
            item['countryLink'] = response.css('.rdr-info-cont a::attr(href)')[0].getall()
            item['riderDetails'] = response.css('.rdr-img-cont a::attr(href)').getall()
            item['riderImg'] = response.css('.rdr-img-cont a img::attr(src)').getall()
            item['birth'] = response.css('.rdr-info-cont::text').getall()
            item['placeOfBirth'] = response.css('.rdr-info-cont span span a::text')[0].getall()
            item['height'] = response.css('.rdr-info-cont span::text')[1].getall()
            item['wigtht'] = response.css('.rdr-info-cont span::text')[0].getall()
            item['breakDown'] = response.css('.rdr-info-cont span span div a::attr(href)')[0].getall()
            item['dataType'] = response.css('.pps span div::attr(data-type)').getall()
            item['ppsPoint'] = response.css('.pps li  span::text').getall()
            item['socialNetLink'] = response.css('.rdr-info-cont span span div a::attr(href)').re(r'^http.+')
            item['pcsRankLink'] = response.css('.rdr-info-cont span span div a::attr(href)').re(r'^rank.+')[0]
            item['worldRankLink'] = response.css('.rdr-info-cont span span div a::attr(href)').re(r'^rank.+')[1]
            item['pcsRank'] = response.css('.rdrStandings span::text')[0].getall()
            item['uciRank'] = response.css('.rdrStandings span::text')[2].getall()
            yield item

        '''riderName = scrapy.Field()
    teamName = scrapy.Field()
    country = scrapy.Field()
    riderCountryFlag = scrapy.Field()
    countryLink = scrapy.Field()
    riderDetails = scrapy.Field()
    riderImg = scrapy.Field()
    birth = scrapy.Field()
    height = scrapy.Field()
    wigtht = scrapy.Field()
    placeOfBirth = scrapy.Field()
    breakDown = scrapy.Field()
    dataType = scrapy.Field()
    ppsPoint = scrapy.Field()
    socialNetLink = scrapy.Field()
    pcsRankLink = scrapy.Field()
    worldRankLink = scrapy.Field()
    pcsRank = scrapy.Field()
    uciRank = scrapy.Field()'''

        #bio

        #riderName = response.css('div.content div.entry h1::text').get()
        #teamName = response.css('div.content div.entry h1 span::text')[1].getall()
        #riderCountryFlag = response.css('div.content div.entry span::attr(class)')[0].getall()
        #riderDetails = response.css('.rdr-img-cont a::attr(href)').getall()
        #riderImg = response.css('.rdr-img-cont a img::attr(src)').getall()
        #birth = response.css('.rdr-info-cont::text').getall()
        #countryLink = response.css('.rdr-info-cont a::attr(href)')[0].getall()
        #country = response.css('.rdr-info-cont a::text')[0].getall()
        #height = response.css('.rdr-info-cont span::text')[1].getall()
        #wigtht = response.css('.rdr-info-cont span::text')[0].getall()
        #placeOfBirth = response.css('.rdr-info-cont span span a::text')[0].getall()
        #breakDown = response.css('.rdr-info-cont span span div a::attr(href)')[0].getall()
        #dataType = response.css('.pps span div::attr(data-type)').getall()
        #ppsPoint = response.css('.pps li  span::text').getall()
        #socialNetLink = response.css('.rdr-info-cont span span div a::attr(href)').re(r'^http.+')
        #pcsRankLink = response.css('.rdr-info-cont span span div a::attr(href)').re(r'^rank.+')[0]
        #worldRankLink = response.css('.rdr-info-cont span span div a::attr(href)').re(r'^rank.+')[1]
        #uciRankLink = response.css('.rdr-info-cont span span div a::attr(href)').re(r'^rank.+')[2]
        #pcsRank =  response.css('.rdrStandings span::text')[0].getall()
        #worldRank = response.css('.rdrStandings span::text')[1].getall()
        #uciRank = response.css('.rdrStandings span::text')[2].getall()