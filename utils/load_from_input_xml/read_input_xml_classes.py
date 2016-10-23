# -*- coding: utf-8 -*-
# encoding=utf8  
import sys, json, re
reload(sys)  
sys.setdefaultencoding('utf8')

path_dir = ""
xml = "paraphrases_gold.xml"
output = "test_res.json"
path_in = path_dir + xml
path_in_json = "../../test.json"
path_out = path_dir + output
f = open(path_in)
line = f.readlines()
f.close()
f = open(path_in_json)
jdata = json.load(f)
f.close()
n = len(line)
tags = ['<value name="class">', '</value>']
classes_names = ["NON-paraphrase", "Near-paraphrase", "Precise-paraphrase"]
x = 0
for i in range(n):
  if line[i].find(tags[0]) >= 0:
    posA = line[i].find(tags[0]) + len(tags[0])
    posB = line[i].find(tags[1])
    if posA < 0 or posB < 0:
      raise Exception("bad format "+ line[i])
    classs = int(line[i][posA:posB])
    jdata[x]['real_class'] = classes_names[classs+1]
    x += 1
print x
f = open(path_out, "w+")
f.write(json.dumps(jdata, sort_keys=True, indent=1, separators=(',', ': '), ensure_ascii=False))
f.close()
