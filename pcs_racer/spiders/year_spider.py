import scrapy
from pcs_racer.items import pcsRacerItem

class PcsSpider(scrapy.Spider):
    name = "year"
    start_urls = [
        'https://www.procyclingstats.com/rider/chad-haga'
    ]

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)


    def parse(self, response):
        for racer in response.css('body'):
            item = pcsRacerItem() 
            item['riderName'] = racer.css('div.content div.entry h1::text').get()
            item['teamName'] = racer.css('div.content div.entry h1 span::text')[1].get()
            item['country'] = racer.css('div.content div.entry span::attr(class)')[0].get()
            item['riderCountryFlag'] = racer.css('div.content div.entry span::attr(class)')[0].get()
            item['countryLink'] = racer.css('.rdr-info-cont a::attr(href)')[0].get()
            item['riderDetails'] = racer.css('.rdr-img-cont a::attr(href)').get()
            item['riderImg'] = racer.css('.rdr-img-cont a img::attr(src)').get()
            item['birth'] = racer.css('.rdr-info-cont::text').get()
            item['placeOfBirth'] = racer.css('.rdr-info-cont span span a::text')[0].get()
            item['height'] = racer.css('.rdr-info-cont span::text')[1].get()
            item['wigtht'] = racer.css('.rdr-info-cont span::text')[0].get()
            item['breakDown'] = racer.css('.rdr-info-cont span span div a::attr(href)')[0].get()
            item['dataType'] = racer.css('.pps span div::attr(data-type)').get()
            item['ppsPoint'] = racer.css('.pps li  span::text').getall()
            item['socialNetLink'] = racer.css('.rdr-info-cont span span div a::attr(href)').re(r'^http.+')
            item['pcsRankLink'] = racer.css('.rdr-info-cont span span div a::attr(href)').re(r'^rank.+')[0]
            item['worldRankLink'] = racer.css('.rdr-info-cont span span div a::attr(href)').re(r'^rank.+')[1]
            item['pcsRank'] = racer.css('.rdrStandings span::text')[0].get()
            item['uciRank'] = racer.css('.rdrStandings span::text')[2].get()
            #Top result
            item['stageOrGc'] = response.css('ul.moblist div span.blue::text').get()
            item['topResultRace'] = response.css('ul.moblist div a::text').getall()
            item['raceType'] = response.css('ul.moblist div span.blue::text').getall()
            item['raceRank'] = response.css('ul.moblist div::text').getall()
            item['yearOfRace'] = response.css('ul.moblist div span::text').re(r'(\'\d.)')
            #Teams
            item['team'] = response.css('div.div2 ul li span a::text').getall()
            item['yearOfTeam'] = response.css('div.div2 ul li span::text').re(r'\d{4}')
            #Key statistics
            item['keystatistics'] = response.css('div.div2 ul.key-stats li div a::text').getall()
            item['keyNumber'] =  response.css('div.div2 ul.key-stats li div::text').getall()
            item['keyword'] = response.css('div.div2 ul.key-stats li div span::text').getall()
            #PCS Ranking position per season
            item['season'] = response.css('div.div4 ul.ranking-per-season li div.season a::text').getall()
            item['rps_points'] = response.css('div.div4 ul.ranking-per-season li div.bar div::text').getall()
            item['rps_pos'] = response.css('div.div4 ul.ranking-per-season li div.pos::text').getall()
            #Results per season
            item['season'] = response.css('div.div3 ul.horiztree li a::text').getall()
            item['seasonLink'] = response.css('div.div3 a.seasonResults::attr(href)').getall()

            yield item

        allYears = response.xpath(".//a[@class=seasonResults]//@href").getall()
        for singleYear in allYears:
            if singleYear is not None:
                yield response.follow(singleYear, self.parse)
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
        
        
#Top result
    #stageOrGc = response.css('ul.moblist div span.blue::text').get()
    #topResultRace = response.css('ul.moblist div a::text').getall()
    #raceType = response.css('ul.moblist div span.blue::text').getall()
    #raceRank = response.css('ul.moblist div::text').getall()
    #yearOfRace = response.css('ul.moblist div span::text').re(r'(\'\d.)')
#Teams
    #team = response.css('div.div2 ul li span a::text').getall()
    #yearOfTeam = response.css('div.div2 ul li span::text').re(r'\d{4}')
#Key statistics
    #keystatistics = response.css('div.div2 ul.key-stats li div a::text').getall()
    #keyNumber =  response.css('div.div2 ul.key-stats li div::text').getall()
    #keyword = response.css('div.div2 ul.key-stats li div span::text').getall()
#PCS Ranking position per season
    #season = response.css('div.div4 ul.ranking-per-season li div.season a::text').getall()
    #rps-points = response.css('div.div4 ul.ranking-per-season li div.bar div::text').getall()
    #rps-pos = response.css('div.div4 ul.ranking-per-season li div.pos::text').getall()
#Results per season
    #season = response.css('div.div3 ul.horiztree li a::text').getall()
    #seasonLink = response.css('div.div3 a.seasonResults::attr(href)').getall()
#prresHead
    #prresHead = response.css('div.results ul.prresHead li::text').getall()
#prres = response.css('ul.prres')
    #prresDate = prres.css('li div::text')[0].get()
    #prresEndDate = prres.css('li div span::text')[0].get()
    #prresFlag = prres.css('li div span.flag').getall()
    #prresLink = prres.css('li div a::attr(href)')[0].getall()
    #prresName = prres.css('li div a b::text')[0].get()
    #prresLevel = prres.css('li div a::text')[0].getall()
    
    #First
    #prresRangeFirst = prres.css('li ul li div::text')[0].get()
    #prresShirtFirst = prres.css('li ul li div span::attr(class)')[0].get()
    #prresShirtNameLinkFirst = prres.css('li ul li div a::attr(href)')[0].get()
    #prresShirtNameFirst = prres.css('li ul li div a::text')[0].get()

    #Second
    #prresRangeSecond = prres.css('li ul li div::text')[1].get()
    #prresShirtSecond = prres.css('li ul li div span::attr(class)')[1].get()
    #prresShirtNameLinkSecond = prres.css('li ul li div a::attr(href)')[1].get()
    #prresShirtNameSecond = prres.css('li ul li div a::text')[1].get()

    #Third
    #prresRangeSecond = prres.css('li ul li div::text')[2].get()
    #prresShirtSecond = prres.css('li ul li div span::attr(class)')[2].get()
    #prresShirtNameLinkSecond = prres.css('li ul li div a::attr(href)')[2].get()
    #prresShirtNameSecond = prres.css('li ul li div a::text')[2].get()

    #dateList = prres.css('li ul li div::text').getall()
    #stageList = prres.css('li ul li div a::text').getall()
    #

#prres table 
#prres=response.xpath("//ul[@class='prres']")
#date
#for div in prres.xpath('.//div[1]'):
#    print(div.xpath('.//text()').getall())
#race
#for div in prres.xpath('.//div[5]'):
#          print(div.xpath('.//text()').getall())
#race link
#for div in prres.xpath('.//div[5]'):
#    print(div.xpath('.//a//@href').getall())
#race result 
#for div in prres.xpath('.//ul//li'):
#         print(div.xpath('.//div[2]//text()').get(''))
#race distance
#for div in prres.xpath('.//ul//li'):
#         print(div.xpath('.//div[6]//text()').get(''))
#pcs point
# for div in prres.xpath('.//ul//li'):
#         print(div.xpath('.//div[7]//text()').get(''))
#uci point
#for div in prres.xpath('.//ul//li'):
#         print(div.xpath('.//div[8]//text()').get(''))
#race more detail
#for div in prres.xpath('.//li'):
#         print(div.xpath('.//div[9]//a//@href').get(''))
