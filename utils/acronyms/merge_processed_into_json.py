# -*- coding: UTF-8 -*-
# encoding=utf8  
import sys, json  
reload(sys)  
sys.setdefaultencoding('utf8')
from pprint import pprint

with open('data/out1.txt.bk') as data_file:    
  new_sentences = data_file.readlines()
print len(new_sentences), len(new_sentences)/3.0
with open('../../dataset.json') as data_file:    
  jlist = json.load(data_file)


list_dict_res = []
for i in range(7227):
  tmp = [a for a in jlist if int(a['id'])==i+1][0]
  tmp["source_acronym_resolved"] = [new_sentences[i*3], new_sentences[i*3+1]]
  list_dict_res.append(tmp)
  print i

f = open("database_new.json", "w+")
f.write(json.dumps(list_dict_res, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
f.close()
