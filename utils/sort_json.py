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
data_copy = list(data)
N = len(data_copy)
sorted(data_copy, key = lambda x: x['id'])
print json.dumps(data_copy, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False).encode('utf8')

