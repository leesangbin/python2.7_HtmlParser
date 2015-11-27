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






#html = urllib2.urlopen(targetUrl)

f = open("bootstrap2.html", "r")

html = f.read()
# print (html)


#print html
#html = urllib.urlopen('http://comic.naver.com/webtoon/weekday.nhn')
#soup = BeautifulSoup(html, "lxml")
# soup = BeautifulSoup(open("bootstrap2.html"))
# soup = BeautifulSoup(open("bootstrap2.html"), "lxml")
file_name ='bootstrap2.html' #---------------------------------------------------------------- step1 set file name
html_doc = open(file_name)
# soup = BeautifulSoup(html_doc, "html.parser")
soup = BeautifulSoup(html_doc, "lxml")


# tag= soup.find(id="dropdown")
# tag= soup.find("section", id="dropdown")
# tag= soup.find_all("div","page-header")


# tag= soup.section
# tag= soup.div

# tag['id']='directives_small'
# tag['class']='col-md-6'
# tag['class']='row'
# tag['id']='dropdown'


print '--------------'
# print len(tag.contents)
print '--------------'
# print tag.contents
print '--------------'
# print tag.prettify()
# tag = soup.find_all(attrs={"class":"page-header"})
tag = soup.find_all("div", attrs={"class":"row"})

# code = soup.div.ul.li.code
# em = soup.div.ul.li.em
# string= soup.div.ul.li.string
# em= soup.find_all(attrs={"class":"col-md-6"}).find_all("ul").find_all("li").find_all("em")
# string= soup.find_all(attrs={"class":"col-md-6"}).find_all("ul").find_all("li").string
# <div class="col-md-6">
# print tag

# print (tag)

print '--------------'
# print code
print '--------------'
# print em
print '--------------'
# print string
print tag
#soup = BeautifulSoup(html.read())
# print soup.prettify()
#titles = soup.find_all("a", "title")
#section_ids = soup.find_all("section", "id")
#titles = soup.find_all("a", "href")
# titles = soup.find_all('li')
# titles = soup.section['id']

#<section id="accordion">

# for title in titles:
#     print str(title)
  #  print 'section_id:{0:10s} \n'.format(section_id['id'].encode('utf-8'))
#    print 'title:{0:10s} link:{1:20s}\n'.format(title['title'].encode('utf-8'), title['href'].encode('utf-8'))
