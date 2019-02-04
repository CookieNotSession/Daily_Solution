#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 15:53:21 2019

@author: cookiehiker
"""
import urllib.request as req
url = 'https://www.ptt.cc/bbs/movie/index.html'

# build a request object , with 'Request Headers' data

request = req.Request(url, headers = {
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

# parsing source code , and get the title of every post in PTT.

import bs4
root = bs4.BeautifulSoup(data, "html.parser")
titles = root.find_all("div", class_="title") # find all tag div about class="title"
for title in titles :
    if title.a != None : # if title with tag a (which mean it's not deleted). print it!
        print(title.a.string)