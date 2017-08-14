import os
#from urllib.parse import urljoin
#from urllib.parse import urljoin
import urllib.request

from hashlib import md5
from lxml.html import parse

tree = parse('http://www.imdb.com/chart/top')
movies = tree.xpath("//table[contains(@class, 'chart')]//td[@class='titleColumn']//a")
for movie in movies:
    url = urllib.request.urljoin('http://www.imdb.com/', movie.get('href'))
    img = tree.xpath("//td[contains(@id,'img_primary')]//img/@src").extract()
print(url)
print(img)
