# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 09:35:35 2018

@authors: MrWormsy (AKA Antonin ROSA-MARTIN), Loick Combrie, Lucile Delage and David Petit
"""
from urllib.request import urlopen

html = urlopen("http://capsules.musa.free.fr/Caves02.html")

import bs4 as BeautyfulSoup

import re

import pandas as pandas

soup = BeautyfulSoup.BeautifulSoup(html, 'html.parser')

ref = soup.find_all("b")

newRefs = []

regex1 = re.compile(r'(href)')
regex2 = re.compile(r'(-1)')

for r in ref:
    
    if(regex1.search(str(r)) and regex2.search(str(r))):
        test = str(r).split("html\">")
        test = re.sub(r'<font size="-1">', '', test[1])
        test = re.sub(r'[A-B]\.', '', test)
        test = re.sub(r'<font face=\"Arial,Helvetica\">', '', test)
        test = re.sub(r'(<\/font>)+<\/b>', '', test)
        test = re.sub(r'(</[a-z]+>)', '', test)
        test = re.sub(r'<font color=\"#[0-9]+\">', '', test)
        test = re.sub(r'<u>', '', test)
        test = re.sub(r'&amp;', '&', test)
        test = re.sub(r'_+', '', test)
        test = re.sub(r'\)', '', test)        
        test = test.split("(")
        if(len(test) == 2):
            test1 = re.sub(r'[\n]*[\r]*', '', test[0])
            test2 = test[1]
            newRefs.append([test1, test2])
            
            
            
print(len(newRefs))

df = pandas.DataFrame(newRefs)
df.to_csv("champ.csv")