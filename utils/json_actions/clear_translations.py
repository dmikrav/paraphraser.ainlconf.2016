# -*- coding: utf-8 -*-
# encoding=utf8  
import sys, json, re
reload(sys)  
sys.setdefaultencoding('utf8')

if __name__ == "__main__":
    f = open("../../dataset.json")
    dict_main = json.load(f)
    f.close()
    n = len(dict_main)
    for i in range(n):
      dict_main[i]['translations'] = {}
    f = open("dataset_res.json", "w+")
    f.write(json.dumps(dict_main, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
    f.close()
