#!/usr/bin/env python
# -*- coding: utf-8 -*-

#python scrap_emol.py > input.txt
#pip install beautifulsoup4 soporta python3
#pip install lxml

from urllib.request import urlopen    #para p3
from bs4 import BeautifulSoup
import ssl

context = ssl._create_unverified_context()

page = urlopen('http://elmostrador.cl', context=context).read()
soup = BeautifulSoup(page,'lxml')
mostViewed = soup.findAll("div",
                         {"class": "row"})    #############OBTENIDO MEDIANTE ANALISIS DEL OBJETO EN PARTICULAR
print("##############################################")
urlViewed = []
for div in mostViewed:
    if div.a:
        urlViewed.append(div.a["href"])

####Mostrar links de las noticias obtenidas
#print(urlViewed)

count = 1
for url in urlViewed:
    print("### Noticia {}: ".format(count))
    try:
        page = urlopen("{}".format(url), context=context).read()
        soup = BeautifulSoup(page)
    except:
        print("--")
    print("Título: ")
    try:
        title = soup.find("h2",
                         {"class": "titulo-single"})
        print(title.getText())
        print("Contenido: ")
        try:
                content = soup.find("div",
                                {"id": "noticia"})
                print(content.getText())
        except:
                print("--")
    except:
        print("--")

    print("")
    count += 1
