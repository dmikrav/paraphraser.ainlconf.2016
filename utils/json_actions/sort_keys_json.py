import json
# -*- coding: utf-8 -*-
# encoding=utf8  
import sys, json, re
reload(sys)  
sys.setdefaultencoding('utf8')
dpath = "../../"

#name = "dataset"
name = "test"

f = open(dpath+name+".json")
jdata = json.load(f)
f.close()
f = open(dpath+name+"_sorted.json", "w+")
f.write(json.dumps(jdata, indent=1, separators=(',', ': '), ensure_ascii=False, sort_keys=True))
f.close()
