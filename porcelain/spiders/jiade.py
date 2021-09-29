import scrapy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from porcelain.items import jiadeItems


browser = webdriver.Chrome()


class JiadeSpider(scrapy.Spider):
    name = 'jiade'
    allowed_domains = ['cguardian.com']
    start_urls = ['https://www.cguardian.com/Auctions/AuctionResult']

    def parse(self, response):
        try:
            browser.get(self.start_urls[0])
            all_url_count = int(browser.find_element_by_xpath(
                '//*[@id="app"]/div/div[2]/div/div[3]/div[2]/div[12]/div/span/div/input'
            ).get_attribute('max'))
            for page in range(1, all_url_count):
                self.page_click(browser, page)
                for item in range(2, 12):
                    be_re = f'//*[@id="app"]/div/div[2]/div/div[3]/div[2]/div[{str(item)}]'
                    be_item_click = browser.find_element_by_xpath(be_re)
                    be_item_click.click()
                    all_items_count = len(browser.find_elements_by_xpath('//div[@class="category-list-border"]/div'))
                    for i in range(1, all_items_count+1):
                        be_item_re = be_re + f'/div[2]/div[{str(i)}]'
                        self.item_click(browser, be_item_re)
                        self.parse_data(browser)

                        be_item_ocunt = int(browser.find_element_by_xpath('//*[@id="item-content"]/div[2]/div/span/div/input').get_attribute('max'))
                        for j in be_item_ocunt(1, be_item_ocunt+1):
                            new_item_page = browser.find_element_by_xpath('//*[@id="item-content"]/div[2]/div/span/div/input')
                            new_item_page.clear()
                            new_item_page.send_keys(j)
                            new_item_page.send_keys(Keys.ENTER)
                            self.parse_data(browser)
                        browser.back()


        except Exception as e:
            print(e)


    def page_click(self, browser, page):
        page_click = browser.find_element_by_class_name('el-input__inner')
        page_click.clear()
        page_click.send_keys(page)
        page_click.send_keys(Keys.ENTER)

    def item_click(self, browser, be_item_re):
        item = browser.find_element_by_xpath(be_item_re)
        item.click()

    def parse_data(self, browser):
        pa_data = browser.find_elements_by_xpath('//*[@id="item-content"]/div/div')
        for item in pa_data:
            item = item.text
            item_list = item.splitlines()
            if item_list is not None:
                jiadeItems['num'], jiadeItems['name'], jiadeItems['date'], jiadeItems['price'] = item_list





