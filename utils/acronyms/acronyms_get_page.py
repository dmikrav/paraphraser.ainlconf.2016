# encoding: utf-8
# coding: utf-8

listt = ["https://ru.wiktionary.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%90%D0%B1%D0%B1%D1%80%D0%B5%D0%B2%D0%B8%D0%B0%D1%82%D1%83%D1%80%D1%8B/ru&pageuntil=%D0%92%D0%9A%D0%9A%0A%D0%92%D0%9A%D0%9A#mw-pages", 

"https://ru.wiktionary.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%90%D0%B1%D0%B1%D1%80%D0%B5%D0%B2%D0%B8%D0%B0%D1%82%D1%83%D1%80%D1%8B/ru&pagefrom=%D0%92%D0%9A%D0%9A%0A%D0%92%D0%9A%D0%9A#mw-pages",

"https://ru.wiktionary.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%90%D0%B1%D0%B1%D1%80%D0%B5%D0%B2%D0%B8%D0%B0%D1%82%D1%83%D1%80%D1%8B/ru&pagefrom=%D0%97%D0%A0%D0%9A%0A%D0%97%D0%A0%D0%9A#mw-pages",

"https://ru.wiktionary.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%90%D0%B1%D0%B1%D1%80%D0%B5%D0%B2%D0%B8%D0%B0%D1%82%D1%83%D1%80%D1%8B/ru&pagefrom=%D0%9D%D0%98%D0%98#mw-pages",

"https://ru.wiktionary.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%90%D0%B1%D0%B1%D1%80%D0%B5%D0%B2%D0%B8%D0%B0%D1%82%D1%83%D1%80%D1%8B/ru&pagefrom=%D0%A1%D0%90%D0%A1%0A%D0%A1%D0%90%D0%A1#mw-pages",

"https://ru.wiktionary.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%90%D0%B1%D0%B1%D1%80%D0%B5%D0%B2%D0%B8%D0%B0%D1%82%D1%83%D1%80%D1%8B/ru&pagefrom=%D0%A4%D0%A1%D0%9A%0A%D0%A4%D0%A1%D0%9A#mw-pages"]

import urllib2, traceback, sys

#sys.setdefaultencoding("UTF-8")

#from nltk.stem.wordnet import WordNetLemmatizer
#import nltk
#import en
#import re, json
#from nltk.stem.lancaster import LancasterStemmer
#stemmer = LancasterStemmer()

def get_meaning(page_url):
  response = urllib2.urlopen(page_url)
  html = response.read().lower()
  tag = [' title="сокращённое">сокр.</span></a> от <a href=', ' title="сокращённое">сокр.</span></a>'] 
  for i in range(2):
    posA = html.find(tag[i]) + len(tag[i])
    if posA == -1 and i == 1:
      return ""
    if posA == -1:
      continue
    posB = html.find(">", posA)
    posC = html.find("<", posB)
  return html[posB+1:posC]

def get_acronyms(page_url): 
  verbose = False
  res = []
  try:
    response = urllib2.urlopen(page_url)
    html = response.read().lower()
    #print html
    tags = ['<div class="mw-category-group">', '</div>'] 
    inside = ['<li><a href="', 'title="']
    posB = 0
    while True:
      posA = html.find(tags[0], posB)
      posB = html.find(tags[1], posA)
      if posA == -1 or posB == -1:
        break
      tmp = html[posA:posB]
      #print tmp
      posF = 0
      while True:
        posC = tmp.find(inside[0], posF)+len(inside[0])
        posD = tmp.find('"', posC)
        posE = tmp.find(inside[1], posD)+len(inside[1])
        posF = tmp.find('"', posE)
        if posC == -1+len(inside[0]) or posD == -1 or posE == -1+len(inside[1]) or posF == -1:
          break
        tmp_b = tmp[posC:posD]
        tmp_c = tmp[posE:posF]
        res.append(["https://ru.wiktionary.org" + tmp_b, tmp_c])
    if verbose: print res 
    if verbose: print "\n", "=" * 80
    if verbose: print html
  except:
    traceback.print_exc(file=sys.stdout)
    return "exception" 
  return res

index = 5
lista = get_acronyms(listt[index])
n = len(lista)
cnt = 0
res = ""
for i in lista:
  cnt += 1
  print cnt, "of", n
  f = open("acronyms/"+"0"+str(index), "a+")
  f.write(i[1] + '\t' + get_meaning(i[0]) + "\n")
  f.close()
