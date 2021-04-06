"""
 This file is part of Sumak.me-django
 Copyright (C) 2021 Asociación SUMAK <info (at) sumakcoop (dot) org

 Sumak.me-django is free software: you can redistribute it and/or modify
 it under the terms of the GNU Affero General Public License as
 published by the Free Software Foundation, either version 3 of the
 License, or (at your option) any later version.

 Sumak.me-django is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU Affero General Public License for more details.

 You should have received a copy of the GNU Affero General Public License
 along with Sumak.me-django.  If not, see <http://www.gnu.org/licenses/>.
"""

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
