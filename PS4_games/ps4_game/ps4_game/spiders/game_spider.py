# -*- coding: utf-8 -*-
import scrapy
from ..items import Ps4GameItem

class GameSpiderSpider(scrapy.Spider):
    name = 'game_spider'
    start_urls = ['https://www.amazon.com/s?k=ps4+games&rh=n%3A6427831011&ref=nb_sb_noss/']
    page_n = 1
    placeholder = "Not Available"
    def parse(self, response):
        items = Ps4GameItem()
        res = response.css("div.s-result-item")
        for q in res:
            name = q.css("span.a-color-base.a-text-normal::text").getall()
            price = q.css("span[data-a-size=l] .a-offscreen").css('::text').getall()
            star = q.css("span.a-icon-alt::text").getall()
            n_sale = q.css(".a-size-small .a-link-normal .a-size-base::text").getall()
            year = q.css(".a-color-secondary.a-text-normal::text").getall()
            plat = q.css(".a-spacing-top-small .a-text-bold::text").getall()


            if plat!=[]:
                tmp = ""
                p_lst = plat[0].split(" ")
                for i in range(len(p_lst)):
                    if p_lst not in ['\n', '']:
                        tmp += p_lst[i]
                tmp = tmp.split('\n')
                for i in range(len(tmp)):
                    if tmp[i] != "":
                        plat = [tmp[i]]

                item_lst = {'name':name, 'price':price, 'star':star, 'n_sale':n_sale, 'year':year, 'plat':plat}
                if plat[0] == "PlayStation4":
                    for key in list(item_lst.keys()):
                        if item_lst[key] == []:
                            items["%s" % key] = GameSpiderSpider.placeholder
                        elif len(item_lst[key]) > 1:
                            items["%s" % key] = item_lst[key][0]
                        else:
                            if key == 'star':
                                item_lst[key] = [item_lst[key][0][:3]]
                            items["%s" % key] = item_lst[key][0]
            yield items
        next_page = "https://www.amazon.com/s?k=ps4+games&i=videogames&rh=n"+"%"+"3A6427831011&page=%d" % GameSpiderSpider.page_n
        if GameSpiderSpider.page_n<=3:
            GameSpiderSpider.page_n+=1
            yield response.follow(next_page,callback = self.parse)
