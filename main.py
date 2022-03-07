import csv

import requests, os
from lxml import etree
import random
import time
from fake_useragent import UserAgent


class Travel(object):
    def __init__(self):
        self.url = "https://place.qyer.com/south-korea/citylist-0-0-{}/"
        self.film_list = []
        ua = UserAgent(verify_ssl=False,use_cache_server=False)
        for i in range(1, 50):
            self.film_list.append(ua.chrome)
            self.Hostreferer = {
                'User-Agent': random.choice(self.film_list)
            }

    def main(self):
        startPage = int(input("起始页:"))
        endPage = int(input("终止页:"))
        for page in range(startPage, endPage + 1):
            url = self.url.format(page)
            print(url)
            html = self.get_page(url)
            print(html)


    def get_page(self, url):
        html = requests.get(url=url, headers=self.Hostreferer).content.decode("utf-8")
        self.page_page(html)

    def page_page(self, html):
        parse_html = etree.HTML(html)
        image_src_list = parse_html.xpath('//ul[@class="plcCitylist"]/li')
        for i in image_src_list:
            b = i.xpath('.//h3//a/text()')[0].strip()
            print(b)
            c = i.xpath('.//p[@class="beento"]//text()')[0].strip()
            print(c)
            d = i.xpath('.//p[@class="pics"]//img//@src')[0].strip()
            print(d)
            # 创建csv文件进行写入
            csv_file = open('scrape.csv', 'a', encoding='gbk')
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([b, c, d])
            csv_file.close()


if __name__ == '__main__':
    spider = Travel()
    spider.main()
