# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 09:35:35 2018

@authors: MrWormsy (AKA Antonin ROSA-MARTIN), Loick Combrie, Lucile Delage and David Petit
"""
from urllib.request import urlopen

html = urlopen("https://database.lichess.org")

import bs4 as BeautyfulSoup

import re

soup = BeautyfulSoup.BeautifulSoup(html, 'html.parser')

ref = soup.find_all("a")

newRefs = []

regex = re.compile(r'(standard\/lichess_db_standard_rated_)([0-9]+\-[0-9]+)(\.pgn\.bz2)')

for r in ref:
    if(regex.search(str(r))):
        newRefs.append(str(r))
    
print(newRefs.__len__())