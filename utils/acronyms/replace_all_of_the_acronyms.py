# -*- coding: UTF-8 -*-
# encoding=utf8  
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

import json
from pprint import pprint


#################################################
f = open("data/all.txt")
all_data = f.readlines()
f.close()

all_data_key_value = []
all_data_dict = {}
for line in all_data:
  l = line.split("\t")
  all_data_key_value.append(l)
  all_data_dict[unicode(l[0])] = unicode(l[1])[:-1]
all_data_keys = []
for i in range(len(all_data_key_value)):
  tmp = unicode(all_data_key_value[i][0], 'utf-8')
  all_data_keys.append(tmp)

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
      #print w, "\t", key_value[1][:-1]
      flag = True
      found_cnt += 1
      break
  if not flag:
    absent_list.append(w)
    #print w, "\t", "meaning for acronym not found"
print "\n", "Total found =", 100.0*found_cnt/total_cnt, "%"
print "\n", "Absent list:", "\n"
#for w in absent_list:
#  print w+"\t"

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
  

def replace_acronyms(sentence):
  sentence = unicode(sentence)
  listt = sentence.split(" ")
  res = ""
  for a in listt:
    a = unicode(a)
    for k in all_data_keys:
      #print k, len(k)
      #k = unicode(k)
      if trim_char_padding(a) == k:
        tmp = a.find(k)
        posA = tmp
        posB = tmp+len(k)
        a = a[:posA] + all_data_dict[k] + a[posB:]
    res += a + " "
  return res[:]
  
sys.stderr.write("ver.1\n")
with open('../../test.json') as data_file:    
  data = json.load(data_file)
data_copy = list(data)
N = len(data_copy)
print "N:", N
sources = [a["source"] for a in data_copy]
cnt = 0
for pair in sources:
  sys.stderr.write(str(cnt)+"\n")
  cnt += 1
  for i in range(2):
    pair[i] = replace_acronyms(pair[i])
    print unicode(pair[i])
  print

