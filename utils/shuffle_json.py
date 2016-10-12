# -*- coding: UTF-8 -*-
# encoding=utf8  
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')
from pprint import pprint
from random import shuffle
import json
with open('../dataset.json') as data_file:    
  data = json.load(data_file)
'''
for i in range(len(data)):
  data[i]['source'][0] = unicode(data[i]['source'][0])
  data[i]['source'][1] = unicode(data[i]['source'][1])
'''
data_copy = list(data)
N = len(data_copy)
'''
print "N:", N
print "NON-paraphrase", len([a for a in data_copy if a["class"] == "NON-paraphrase"])
print "Precise-paraphrase", len([a for a in data_copy if a["class"] == "Precise-paraphrase"])
print "Near-paraphrase", len([a for a in data_copy if a["class"] == "Near-paraphrase"])
'''
for i in range(3):
  shuffle(data_copy)

print json.dumps(data_copy, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False).encode('utf8')

