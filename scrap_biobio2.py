#!/usr/bin/env python
# -*- coding: utf-8 -*-


#pip install beautifulsoup4 soporta python3
#pip install lxml

from urllib.request import urlopen    #para p3
from bs4 import BeautifulSoup
import ssl

context = ssl._create_unverified_context()

page = urlopen('https://www.biobiochile.cl/lista/categorias/nacional', context=context).read()
soup = BeautifulSoup(page,'lxml')
Nacional = soup.findAll("div",
                         {"class": "noticia row"})

#print("####################CAPTURA PAGINA##################################")
#print(Nacional)

urlViewed = []
for div in Nacional:
    if div.a:
        urlViewed.append(div.a["href"])

#print("#############LISTADO DE NOTICIAS CON URL############################")
#Listado de direcciones con noticias url
#print(urlViewed)

count = 1
for url in urlViewed:
    print("### Noticia {}: ".format(count))
    try:
        page = urlopen("{}".format(url), context=context).read()	#apertura de la url
        soup = BeautifulSoup(page)    					#Extraccion de todo el contenido de la url
    except:
        print("Error al intentar recuperar noticia.")
    print("Título: ")
    try:
        title = soup.find("div",
                         {"class": "nota-titular robotos"})
        print(title.getText())
    except:
        print("Error al intentar recuperar Título noticia.")
    print("Contenido: ")
    try:
        content = soup.find("div",
#                         {"class": "noticia row"})
                         {"class": "nota-contenido text-19 robotos"})
        print(content.getText())
    except:
        print("Error al intentar recuperar contenido de noticia.")
    print("")
    count += 1
