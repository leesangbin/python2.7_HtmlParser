'''
Created on 2015. 11. 26.

@author: Administrator
'''
#import urllib
from bs4 import BeautifulSoup
import urllib2


#try:

#targetUrl="https://199.27.79.133/bootstrap"
#targetUrl="https://199.27.79.133/bootstrap"
#targetUrl="http://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start"
targetUrl="http://angular-ui.github.io/bootstrap/"
#<addinfourl at 50191216 whose fp = <socket._fileobject object at 0x02FF8BB0>>
#targetUrl="http://www.naver.com"
#targetUrl="http://jihoo9.iptime.org/#/"
#targetUrl="http://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start"
#targetUrl="http://comic.naver.com/webtoon/weekday.nhn"
html = urllib2.urlopen(targetUrl)

#print html
#html = urllib.urlopen('http://comic.naver.com/webtoon/weekday.nhn')
soup = BeautifulSoup(html, "lxml")
#soup = BeautifulSoup(html.read())
print soup.prettify()
#titles = soup.find_all("a", "title")
#section_ids = soup.find_all("section", "id")
titles = soup.find_all("a", "href")

#<section id="accordion">

for title in titles:
    print str(title)
  #  print 'section_id:{0:10s} \n'.format(section_id['id'].encode('utf-8'))
#    print 'title:{0:10s} link:{1:20s}\n'.format(title['title'].encode('utf-8'), title['href'].encode('utf-8'))
