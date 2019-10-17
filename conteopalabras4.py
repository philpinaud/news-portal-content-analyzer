# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb
import nltk
import codecs
import sys
sys.stdout.encoding

#####DESCARGA DE REPOSITORIOS IMPORTANTES#####################################################
nltk.download('punkt')
nltk.download('stopwords')


#!/usr/bin/env python
# coding=UTF-8
#
#USO:
#./programa.py input.txt
#
#OBSERVACIONES (PARA CARGAR LIBRERIAS PREVIAS):
# python
# >>> import nltk
# >>> nltk.download('stopwords')
# >>> nltk.download('punkt')
# >>> exit()

######################ELIMINAR STOPWORDS####################################################
from nltk.corpus import stopwords

#USO DE NLTK EN ESPANOL
default_stopwords = set(nltk.corpus.stopwords.words('spanish'))

#DEBE TENER FORMATO DE 01 STOPWORD POR LINEA
stopwords_file = codecs.open('stopwords.txt', 'r', 'latin-1')
#print(stopwords_file.read())
custom_stopwords = set(stopwords_file.read().splitlines())
#print(custom_stopwords)

all_stopwords = default_stopwords | custom_stopwords
#all_stopwords = default_stopwords

input_file = sys.argv[1]

fp = codecs.open(input_file, 'r', 'utf-8')
fp = open(input_file, 'r')

words = nltk.word_tokenize(fp.read())

######################LIMPIEZA###########################################################
#REMOVER CARACTERES UNICOS (PUNTUACION)
words = [word for word in words if len(word) > 1]

#REMOVER NUMEROS
words = [word for word in words if not word.isnumeric()]

#HACER MINUSCULAS TODAS LAS PALABRAS
words = [word.lower() for word in words]

#REMOVER STOPWORDS
words = [word for word in words if word not in all_stopwords]

######################################DETOKENIZAR##########################################
#print(words)
from nltk.tokenize.treebank import TreebankWordDetokenizer
texto = TreebankWordDetokenizer().detokenize(words)
print(texto)


############################NUBE DE TEXTO AUTOMATICA##########################################
from wordcloud import WordCloud
# Generate a word cloud image
wordcloud = WordCloud().generate(texto)

#Display the generated image:
#the matplotlib way:
#import matplotlib.pyplot as plt
#plt.imshow(wordcloud, interpolation='bilinear')
#plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=120, background_color="white", width=1600, height=800).generate(texto)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

#EN CASO DE USAR PIL
#image = wordcloud.to_image()
#image.show()

######################CALCULOS###########################################################
#CALCULO DE LA DISTRIBUCION DE FRECUENCIAS
fdist = nltk.FreqDist(words)

palabras 	= np.array([])
frecuencias 	= np.array([])

#GUARDAR LAS PRIMERAS 50 PALABRAS MAS REPETIDAS
for word, frequency in fdist.most_common(50):
    print(u'{};{}'.format(word, frequency))
    palabras 	= np.append(palabras, word)
    frecuencias	= np.append(frecuencias, frequency)

print(palabras, frecuencias)

#####################GRAFICOS##############################################################
cmap = plt.get_cmap('Spectral')
colors = [cmap(i) for i in np.linspace(0, 1, len(frecuencias))]

import matplotlib
matplotlib.rcParams['text.color'] = 'k'
matplotlib.rcParams['font.size'] = 12
#matplotlib.rcParams['lines.linewidth'] = 8
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

#El argumento maximo es siempre el primero
#print(np.argmax(frecuencias))
#Extraer trozo con el valor mayor para el grafico
explode 	= np.zeros(len(frecuencias))
explode[0] 	= 0.1
print(explode)

fig1, ax1 = plt.subplots()
ax1.pie(frecuencias, labels=palabras, autopct='%1.2f%%', shadow=False, startangle=45, colors=colors, explode=explode)
ax1.axis('equal') 

plt.show()

#####################GRAFICOS##############################################################
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1) # nrows, ncols, index

#Invertir para que quede decreciente y seleccion de 10 mejores resultados
palabras = np.flip(palabras[0:20])
frecuencias = np.flip(frecuencias[0:20])

plt.barh(palabras,frecuencias, color='darkblue', alpha=0.5)
plt.grid(False)
plt.title("TOP 20 PALABRAS")

ax = plt.gca()
fig.patch.set_facecolor('xkcd:white')  ####COLOR EXTERNO
ax.set_facecolor('xkcd:white')	####COLOR INTERNO


plt.show()

