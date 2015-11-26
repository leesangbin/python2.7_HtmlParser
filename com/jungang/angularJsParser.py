'''
Created on 2015. 11. 26.

@author: Administrator
'''
#-*- coding: cp949 -*-
import urllib
from bs4 import BeautifulSoup


targetUrl="http://comic.naver.com/webtoon/weekday.nhn"
html = urllib.urlopen(targetUrl)
#html = urllib.urlopen('http://comic.naver.com/webtoon/weekday.nhn')
#html = urllib.urlopen('http://comic.naver.com/webtoon/weekday.nhn')
soup = BeautifulSoup(html, "lxml")
titles = soup.find_all("a", "title")

for title in titles:
    print 'title:{0:10s} link:{1:20s}\n'.format(title['title'].encode('utf-8'), title['href'].encode('utf-8'))