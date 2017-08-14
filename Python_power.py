import win32com.client

# Open PowerPoint
Application = win32com.client.Dispatch("PowerPoint.Application")

# Add a presentation
Presentation = Application.Presentations.Add()

# Add a slide with a blank layout (12 stands for blank layout)
Base = Presentation.Slides.Add(1, 12)

# Add an oval. Shape 9 is an oval.
oval = Base.Shapes.AddShape(9, 100, 100, 100, 100)



from lxml.html import parse

tree = parse('http://www.imdb.com/chart/top')
##movies = tree.xpath("//table[@class, 'chart']//td[@class='titleColumn']//a")
movies = tree.xpath("//table[contains(@class, 'chart')]//td[@class='titleColumn']//a")
movies[0].text_content()

Base = Presentation.Slides.Add(1, 12)

width, height = 28, 41
for i, movie in enumerate(movies):
    x = 10 + width * (i % 25)
    y = 100 + height * (i // 25)
    r = Base.Shapes.AddShape(1,x, y,width, height)


import os
#from urllib.parse import urljoin
#from urllib.parse import urljoin
import urllib.request

from hashlib import md5

# We'll keep the files under an img/ folder
if not os.path.exists('img'):
    os.makedirs('img')


def filename(movie):
    '''Filename = MD5 hash of its title in UTF8'''
    name = md5(movie.text_content().encode('utf8')).hexdigest()
    return os.path.join('img', name + '.jpg')

for movie in movies:
    if os.path.exists(filename(movie)):
        continue

    url = urllib.request.urljoin('http://www.imdb.com/', movie.get('href'))
    tree = parse(url)
    img = tree.xpath("//td[contains(@id,'img_primary')]//a")
    urllib.request.urlretrieve(img.get('src'), filename(movie))

Base = Presentation.Slides.Add(1, 12)

width, height = 28, 41
for i, movie in enumerate(movies):
    x = 10 + width * (i % 25)
    y = 100 + height * (i // 25)
    image = Base.Shapes.AddPicture(
        os.path.abspath(filename(movie)),
        LinkToFile=True,
        SaveWithDocument=False,
        Left=x, Top=y,
        Width=width, Height=height)
