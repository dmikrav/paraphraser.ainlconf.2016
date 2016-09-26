# -*- coding: UTF-8 -*-

import sys
import json
from pprint import pprint

def trim_char_padding(w):
  res = unicode(w)
  while res != "":
    if not res[0] in [u'А', u'Б', u'В', u'Г', u'Д', u'Е', u'Ё', u'Ж', u'З', u'И', u'Й', u'К', u'Л', u'М', u'Н', u'О', u'П', u'Р', u'С', u'Т', u'У', u'Ф', u'Х', u'Ц', u'Ч', u'Ш', u'Щ', u'Ъ', u'Ы', u'Ь', u'Э', u'Ю', u'Я']:
      res = res[1:]
    else:
      break
  while res != "":
    n = len(res)
    if not res[n-1] in [u'А', u'Б', u'В', u'Г', u'Д', u'Е', u'Ё', u'Ж', u'З', u'И', u'Й', u'К', u'Л', u'М', u'Н', u'О', u'П', u'Р', u'С', u'Т', u'У', u'Ф', u'Х', u'Ц', u'Ч', u'Ш', u'Щ', u'Ъ', u'Ы', u'Ь', u'Э', u'Ю', u'Я']:
      res = res[:-1]
    else:
      break
  return res


def count_big_letters(w):
  cnt = 0
  for c in unicode(w):
    if unicode(c) in [u'А', u'Б', u'В', u'Г', u'Д', u'Е', u'Ё', u'Ж', u'З', u'И', u'Й', u'К', u'Л', u'М', u'Н', u'О', u'П', u'Р', u'С', u'Т', u'У', u'Ф', u'Х', u'Ц', u'Ч', u'Ш', u'Щ', u'Ъ', u'Ы', u'Ь', u'Э', u'Ю', u'Я']:
      cnt += 1
  #if cnt >= 2:
  #  print s, cnt, len(unicode(s))
  #print len(unicode(s))
  return cnt == len(unicode(w)) and cnt >=2


def extract_acronym_only(sentence):
  res = ""
  sentence_lst = sentence.split(" ")
  for w in sentence_lst:
    w = trim_char_padding(w)
    if count_big_letters(w):
      res += w + " "
  return res  
  

with open('../../dataset.json') as data_file:    
  data = json.load(data_file)
data_copy = list(data)
N = len(data_copy)
print "N:", N
	
#with open('data/all.txt') as data_file:    
#  acronyms_data = data_file.read()

#print count_big_letters(u'США')

sources = [a["source"] for a in data_copy]
#res = ""
sentence_with_acronym_cnt = 0
pairs_with_acronym_cnt = 0
for pair in sources:
  #print unicode(pair[0])
  #print unicode(pair[1])
  sentence_with_acronym = [False, False]
  for i in range(2):
    s = extract_acronym_only(unicode(pair[i]))
    if s != "":
      #res += s
      sentence_with_acronym[i] = True
      sentence_with_acronym_cnt += 1
  if sentence_with_acronym[0] and sentence_with_acronym[1]:
    pairs_with_acronym_cnt += 1
#print res
print "sentence_with_acronym_cnt =", sentence_with_acronym_cnt
print "pairs_of_sentences_with_both_acronym_in_them_cnt =", pairs_with_acronym_cnt


