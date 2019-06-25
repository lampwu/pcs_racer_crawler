# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class pcsRacerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    riderName = scrapy.Field()
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
    uciRank = scrapy.Field()

    #Top result
    stageOrGc = scrapy.Field()
    stageOrGc = scrapy.Field() # response.css('ul.moblist div span.blue::text').get()
    topResultRace = scrapy.Field()#response.css('ul.moblist div a::text').getall()
    raceType = scrapy.Field()#response.css('ul.moblist div span.blue::text').getall()
    raceRank = scrapy.Field()#response.css('ul.moblist div::text').getall()
    yearOfRace = scrapy.Field()#response.css('ul.moblist div span::text').re(r'(\'\d.)')
    #Teams
    team = scrapy.Field()#response.css('div.div2 ul li span a::text').getall()
    yearOfTeam = scrapy.Field()#response.css('div.div2 ul li span::text').re(r'\d{4}')
    #Key statistics
    keystatistics = scrapy.Field()#response.css('div.div2 ul.key-stats li div a::text').getall()
    keyNumber = scrapy.Field()#response.css('div.div2 ul.key-stats li div::text').getall()
    keyword = scrapy.Field()#response.css('div.div2 ul.key-stats li div span::text').getall()
    #PCS Ranking position per season
    season = scrapy.Field() #response.css('div.div4 ul.ranking-per-season li div.season a::text').getall()
    rps_points = scrapy.Field() #response.css('div.div4 ul.ranking-per-season li div.bar div::text').getall()
    rps_pos = scrapy.Field() #response.css('div.div4 ul.ranking-per-season li div.pos::text').getall()
    #Results per season
    season = scrapy.Field() #response.css('div.div3 ul.horiztree li a::text').getall()
    seasonLink = scrapy.Field() #response.css('div.div3 a.seasonResults::attr(href)').getall()
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