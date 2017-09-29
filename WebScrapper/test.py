#!/usr/bin/env python
# coding: utf-8
from bs4 import BeautifulSoup
import requests


def parse_contents_href(url, url_args=None, check_content_find=None, tag='a'):
    """
    parse href contents url and find some text in href contents [ for example ]
    """
    html = requests.get(url, params=url_args)
    page = BeautifulSoup.BeautifulSoup(html.text)
    alllinks = page.findAll(tag,  href=True)
    result = check_content_find and filter(
        lambda x: check_content_find in x['href'], alllinks) or alllinks
    return result and "".join(map(str, result)) or False


url = 'http://www.moneycontrol.com/news/business/stocks/page-1/'
if (parse_contents_href(url).find("broker-compare.php")>0):
    print (parse_contents_href(url))