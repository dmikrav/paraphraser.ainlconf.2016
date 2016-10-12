# -*- coding: utf-8 -*-
# encoding=utf8  
import sys, json, re
reload(sys)  
sys.setdefaultencoding('utf8')

import json
f = open("../../test.json")
dict_in = json.load(f)
f.close()
listt = [[a['translations']['yandex']['pair'], a['translations']['microsoft']['pair'], a['translations']['google']['pair']] for a in dict_in]
res = ""
n = len(listt)
for i in range(n):
  res += "======\n"
  for x in range(3):
    for z in range(2):
      res += listt[i][x][z] + "\n"
    res += "\n"
f = open("misc/all-1924.txt", "w+")
f.write(res)
f.close()
