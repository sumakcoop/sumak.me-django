from django.conf.urls import url, include
from oscar import config
import re

# class for overriding default oscar urls
class MyShop(config.Shop):
    def get_urls(self):
        urls = super(MyShop, self).get_urls()
        for index, u in enumerate(urls):
            if u.pattern.regex == re.compile('^catalogue/'):
                urls[index].pattern.regex = re.compile('^catalogo/')
                break
        return urls
