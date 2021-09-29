import scrapy
from scrapy import FormRequest


from porcelain.items import PorcelainItem


class ArtronSpider(scrapy.Spider):
    name = 'artron'
    allowed_domains = ['auction.artron.net']
    start_urls = ['https://auction.artron.net/result/pmp-0-18-0-2-0-0-1/']
    # 模拟登录的cookies
    cookies = {
        '_dg_playback.63d6e55a16491bb2.29f3': '1',
        '_dg_abtestInfo.63d6e55a16491bb2.29f3': '1',
        '_dg_check.63d6e55a16491bb2.29f3': '-1',
        '_dg_antiBotFlag.63d6e55a16491bb2.29f3': '1',
        '_dg_antiBotInfo.63d6e55a16491bb2.29f3': '10%7C%7C%7C3600',
        'Hm_lvt_851619594aa1d1fb8c108cde832cc127': '1630939564',
        'gr_user_id': 'e3def7a9-baa3-446e-934d-436ba7c54b2b',
        '_at_pt_0_': '3162685',
        '_at_pt_1_': '%E6%89%8B%E6%9C%BA%E7%94%A8%E6%88%B73162685',
        '_at_pt_2_': '8c9876d907889f120ba08fb9bd947127',
        '_dg_attr.63d6e55a16491bb2.29f3': '%7B%22userid%22%3A%223162685%22%7D',
        'Hm_lpvt_851619594aa1d1fb8c108cde832cc127': '1631288376',
        '_dg_id.63d6e55a16491bb2.29f3': 'ddbcd0ccaa20cc25%7C%7C%7C1630939564%7C%7C%7C7%7C%7C%7C1631288740%7C%7C%7C1631288721%7C%7C%7C%7C%7C%7Cdfee922ac6ba10a7%7C%7C%7C%7C%7C%7C%7C%7C%7C0%7C%7C%7Cundefined'
    }

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }

        yield FormRequest(url=self.start_urls[0], headers=headers,
                             cookies=self.cookies, callback=self.parse)

    def parse(self, response):
        """
            网页比较工整，直接使用
            '玉器名字': proceleain_name,
            '估算价格': proceleain_Appraisal,
            '实际价格': proceleain_final_price
        """
        items = PorcelainItem()
        Selectors = response.xpath('//*[@id="bigBg"]/div[6]/div[2]/div[2]/div[1]/div[1]/ul/li')
        for item in Selectors:
            proceleain_name = item.xpath('./h3/a/text()').get()
            proceleain_Appraisal = item.xpath('./ul/li[2]/span/text()').get()
            proceleain_final_price = item.xpath('./ul/li[3]/span/text()').get()
            if proceleain_name == None:
                continue
            if proceleain_final_price == None:
                proceleain_final_price = 0
            items['proceleain_name'] = proceleain_name
            items['proceleain_Appraisal'] = proceleain_Appraisal
            items['proceleain_final_price'] = proceleain_final_price
            yield items

        next_page = response.xpath('//*[@id="bigBg"]/div[6]/div[2]/div[2]/div[1]/div[1]/div[2]/a[9]/@href').get()
        if next_page:
            next_url = response.urljoin(next_page)
            yield FormRequest(next_url, callback=self.parse, cookies=self.cookies)
