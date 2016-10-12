# -*- coding: utf-8 -*-
# encoding=utf8  
import sys, json, re
reload(sys)  
sys.setdefaultencoding('utf8')

f = open("../../test.json")
jdata = json.load(f)
f.close()
listt = ["google", "microsoft", "yandex"]
for x in range(3):
  f = open("semilar_metrics/analysis_output_class_" + listt[x] + ".txt")
  lines_semilar = f.readlines()
  f.close()
  for i in range(1924):
    jdata[i]["translations"][listt[x]]["semilar"] = {}
    for y in range(6):
      tmp = lines_semilar[i*10+3+y].split(" : ")
      jdata[i]["translations"][listt[x]]["semilar"][tmp[0]] = tmp[1].replace("\n", "")

f = open("test.json", "w+")
f.write(json.dumps(jdata, sort_keys=True, indent=1, separators=(',', ': '), ensure_ascii=False))
f.close()

