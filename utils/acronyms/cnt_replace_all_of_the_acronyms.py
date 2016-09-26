# -*- coding: UTF-8 -*-

import sys
import json
from pprint import pprint

#################################################
f = open("data/all.txt")
all_data = f.readlines()
f.close()

all_data_key_value = []
for line in all_data:
  all_data_key_value.append(line.split("\t"))
f = open("data/distinct.txt")
distinct_data = f.read()
f.close()
distinct_data = distinct_data.split(" ")
total_cnt = len(distinct_data)
found_cnt = 0
absent_list = []
for w in distinct_data:
  flag = False
  for key_value in all_data_key_value:
    if key_value[0] == w:
      print w, "\t", key_value[1][:-1]
      flag = True
      found_cnt += 1
      break
  if not flag:
    absent_list.append(w)
    print w, "\t", "meaning for acronym not found"
print "\n", "Total found =", 100.0*found_cnt/total_cnt, "%"
print "\n", "Absent list:", "\n"
for w in absent_list:
  print w+"\t"

##############################################################################

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
cnt_of_sentences_with_existing_acronyms = 0
for pair in sources:
  #print unicode(pair[0])
  #print unicode(pair[1])
  sentence_with_acronym = [False, False]
  for i in range(2):
    s = extract_acronym_only(unicode(pair[i]))
    for a in s.split(" "):
      if not a in absent_list:
        cnt_of_sentences_with_existing_acronyms += 1
        break
    if s != "":
      #res += s
      sentence_with_acronym[i] = True
      sentence_with_acronym_cnt += 1
    
  if sentence_with_acronym[0] and sentence_with_acronym[1]:
    pairs_with_acronym_cnt += 1
#print res
print "sentence_with_acronym_cnt =", sentence_with_acronym_cnt
print "pairs_of_sentences_with_both_acronym_in_them_cnt =", pairs_with_acronym_cnt
print "cnt_of_sentences_with_existing_acronyms =", cnt_of_sentences_with_existing_acronyms

