from typing import Iterable
import scrapy
from scrapy.http import Request


class SocialbladeSpiderSpider(scrapy.Spider):
    name = "socialblade_spider"
    headers = {
    "authority": "socialblade.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "referer": "https://socialblade.com/",
    "sec-ch-ua": "\"Chromium\";v=\"118\", \"Microsoft Edge\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46"
    }

    cookies = {
    "PHPSESSXX": "a8bmd0nc46abkel74urrlbonpj"
    }

    def start_requests(self) -> Iterable[Request]:
        yield scrapy.Request(
            url = 'https://socialblade.com/youtube/top/100',
            headers= self.headers,
            cookies= self.cookies,
        )

    def parse(self, response):  
        links = response.xpath('//a[contains(@href , "/youtube/c")]/@href').getall()
        for link in links:
            yield scrapy.Request(
                url = 'https://socialblade.com' + link,
                headers= self.headers,
                cookies= self.cookies,
                callback= self.parse_details
            )

    def parse_details(self, response): 
        channel_name =  response.xpath('//div[@id = "YouTubeUserTopInfoBlockTop"]//h1[1]/text()').get()
        channel_id =  response.xpath('//div[@id = "YouTubeUserTopInfoBlockTop"]//h4[1]//text()').get()
        channel_link = 'https://youtube.com/' + channel_id
        uploads = response.xpath('//span[@id = "youtube-stats-header-uploads"]/text()').get()
        subscribers = response.xpath('//span[@id = "youtube-stats-header-subs"]/text()').get()
        views = response.xpath('//span[@id = "youtube-stats-header-views"]/text()').get()
        country = response.xpath('//span[@id = "youtube-stats-header-country"]/text()').get()
        channel_type = response.xpath('//span[@id = "youtube-stats-header-channeltype"]/text()').get()
        created_date =  response.xpath('//span[contains(text() , "User Created")]/following-sibling::span[1]/text()').get()

        table_data = response.xpath('//p/span[@class= "hint--top"]/text()').getall()
        social_blade_rank = table_data[0].strip()
        subscriber_rank = table_data[1].strip()
        video_view_rank = table_data[2].strip()
        country_rank = table_data[3].strip()
        people_rank = table_data[4].strip()

        estimated_monthly_income = response.xpath('//p[contains(text(), "Estimated Monthly Earnings ")]/preceding-sibling::p/text()').get().replace('\xa0', '').strip()
        subs_last_30_days = response.xpath('//p[contains(text(), "Subscribers for the last 30 days")]/preceding-sibling::p/text()').get().strip()
        views_last_30_days = response.xpath('//p[contains(text(), "Video Views for the last 30 days")]/preceding-sibling::p/text()').get().strip()
        yearly_income = response.xpath('//p[contains(text(), "Estimated Yearly Earnings")]/preceding-sibling::p/text()').get().strip().replace('\xa0', '')

        daily_subs_average = response.xpath('//div[@id="averagedailysubs"]/span/text()').get()
        daily_views_average = response.xpath('//div[@id="averagedailyviews"]/span/text()').get()

        data_dict = {
            'SocialBlade Url' : response.url ,
            'Channel Name': channel_name,
            'Channel ID': channel_id,
            'Channel Link': channel_link,
            'Uploads': uploads,
            'Subscribers': subscribers,
            'Views': views,
            'Country': country,
            'Channel Type': channel_type,
            'Created Date': created_date,
            'Social Blade Rank': social_blade_rank,
            'Subscriber Rank': subscriber_rank,
            'Video View Rank': video_view_rank,
            'Country Rank': country_rank,
            'People Rank': people_rank,
            'Estimated Monthly Income': estimated_monthly_income,
            'Subscribers Last 30 Days': subs_last_30_days,
            'Views Last 30 Days': views_last_30_days,
            'Yearly Income': yearly_income,
            'Daily Subscribers Average': daily_subs_average,
            'Daily Views Average': daily_views_average
        }
        yield data_dict


    

