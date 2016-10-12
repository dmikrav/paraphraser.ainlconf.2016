import json
from pprint import pprint
import string
import os, os.path

printable = set(string.printable)

with open('../test.json') as data_file:    
  data = json.load(data_file)
  
data_copy = list(data)

listt = ["google", "microsoft", "yandex"]
for xx in range(3):
  res = ""
  data_all = [a["translations"][listt[xx]]["pair"] for a in data_copy]
  n = len(data_all)
  for i in range(n):
    res += filter(lambda x: x in printable, data_all[i][0]) + "\n"
    res += filter(lambda x: x in printable, data_all[i][1]) + "\n"
    res += "===\n"
  dirr = "data_extracted_translations"
  if not os.path.exists(dirr):
    os.makedirs(dirr)
  f = open(dirr+"/extracted_"+listt[xx]+".txt", "w+")
  f.write(res)
  f.close()
