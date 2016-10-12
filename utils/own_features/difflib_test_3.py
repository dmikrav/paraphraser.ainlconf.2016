# http://sujitpal.blogspot.co.il/2014/12/semantic-similarity-for-short-sentences.html
from __future__ import division
# -*- coding: utf-8 -*-
# encoding=utf8  
import sys, json, re
import difflib
reload(sys)  
sys.setdefaultencoding('utf8')
import json
sm = difflib.SequenceMatcher(None)
f = open("../../dataset.json")
jdata = json.load(f)
f.close()

n = len(jdata)
brands = ["google", "microsoft", "yandex"]
m = len(brands)
for i in range(n):
  print i
  for x in range(m):
    listt = jdata[i]['translations'][brands[x]]['pair']
    sm.set_seq2(listt[0])
    sm.set_seq1(listt[1])
    jdata[i]['translations'][brands[x]]['difflib'] = [sm.ratio()]  

f = open("dataset.json", "w+")
f.write(json.dumps(jdata, sort_keys=True, indent=1, separators=(',', ': '), ensure_ascii=False))
f.close()
