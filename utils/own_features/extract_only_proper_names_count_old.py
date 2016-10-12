# -*- coding: UTF-8 -*-
# encoding=utf8  
import sys, json  
reload(sys)  
sys.setdefaultencoding('utf8')
from pprint import pprint
import re

def is_proper(s):
  return len(filter(lambda x: (x>='A' and x<='Z'), s)) == 1

def process(s, dictt_prev):
  t = filter(lambda x: (x>='A' and x<='Z') or (x>='a' and x<='z') or x == ' ', s)
  lt = t.split(" ")
  cnt = 0
  same = 0
  dictt = {}
  for x in lt:
    if is_proper(x):
      cnt += 1
      #lenn = len(x)
      #if lenn*0.8 >= 2:
      #  lenn = int(lenn*0.8)
      if x in dictt_prev:
        same += 1
      dictt[x] = 7
  return cnt, same, dictt
      

with open('../../test.json') as data_file:    
  jlist = json.load(data_file)

listt = ['google', 'microsoft', 'yandex']
n = len(jlist)
m = len(listt)
for i in range(n):
  for x in range(m):
    tmp = jlist[i]['translations'][listt[x]]['pair']
    dictt = {}
    cnt_0, same, dictt = process(tmp[0], dictt) 
    cnt_1, same, dictt = process(tmp[1], dictt)
    mn = min(cnt_0, cnt_1)
    mx = max(cnt_0, cnt_1)
    if mn > 0:
      the_same = 1.0*same/mn
    else:
      the_same = 0
    jlist[i]['translations'][listt[x]]['handy_ner'] = {}
    jlist[i]['translations'][listt[x]]['handy_ner']['the_same_proper_nouns_percentage'] = the_same
    jlist[i]['translations'][listt[x]]['handy_ner']['min_proper_nouns_count_in_sentence'] = mn 
    jlist[i]['translations'][listt[x]]['handy_ner']['max_proper_nouns_count_in_sentence'] = mx 


f = open("test_prop.json", "w+")
f.write(json.dumps(jlist, sort_keys=True, indent=1, separators=(',', ': '), ensure_ascii=False))
f.close()
