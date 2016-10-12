import urllib2
import json
from pprint import pprint
import string
import sys
import time
from requests import get
# -*- coding: utf-8 -*-
# encoding=utf8  
import sys, json, re
reload(sys)  
sys.setdefaultencoding('utf8')

sss_url = "http://swoogle.umbc.edu/SimService/GetSimilarity"

def sss(s1, s2, type='relation', corpus='webbase'):
    try:
        response = get(sss_url, params={'operation':'api','phrase1':s1,'phrase2':s2,'type':type,'corpus':corpus})
        return float(response.text.strip())
    except:
        print 'Error in getting similarity for %s: %s' % ((s1,s2), response)
        return 0.0

printable = set(string.printable)

with open('../test.json') as data_file:    
  jdata = json.load(data_file)
  

brands = ["google", "microsoft", "yandex"]
translator_data = [[a["translations"][brands[0]]["pair"] for a in jdata],
                   [a["translations"][brands[1]]["pair"] for a in jdata],
                   [a["translations"][brands[2]]["pair"] for a in jdata]]

translator_data_clean = []

n = len(jdata)
m = len(brands)
for x in range(m):
  tmp_translator_data_clean = []
  for i in range(n):
    tmp = []
    tmp.append(filter(lambda aaa: aaa in printable, translator_data[x][i][0]))
    tmp.append(filter(lambda aaa: aaa in printable, translator_data[x][i][1]))
    tmp_translator_data_clean.append(tmp)
  translator_data_clean.append(tmp_translator_data_clean)

print len(translator_data_clean)
print len(translator_data_clean[0])
print len(translator_data_clean[0][0])

for x in range(m):
  res = ''
  for i in range(n): 
    print x, i
    #sys.stdout.write(brands[x] + ' ' + str(i) + '\n')
    #sys.stdout.flush()
    s0 = translator_data_clean[x][i][0].replace(" ", "%20")
    s1 = translator_data_clean[x][i][1].replace(" ", "%20")
    notFetched = True
    while(notFetched):
      time.sleep(0.02)
      try:
        response = sss(s0, s1)
        notFetched = False
      except:
        #f = open("swoogle/"+brands[x], "w+")
        #f.write(res)
        #f.close()
        #jdata[i]["translations"][brands[x]]["swoogle"] = str(response)
        pass
    jdata[i]["translations"][brands[x]]["swoogle"] = float(str(response))
    #resp = response
    #print resp
    #tmp_res = s0 + '\n' + s1 + '\n' + str(resp) + '\n' + '====================================' + '\n'
    #res += tmp_res
    #print tmp_res
    
  #f = open("swoogle/"+brands[x], "w+")
  #f.write(res.replace("%20", " "))
  #f.close()
  
f = open("test.json", "w+")
f.write(json.dumps(jdata, sort_keys=True, indent=1, separators=(',', ': '), ensure_ascii=False))
f.close()

