# -*- coding: utf-8 -*-
# encoding=utf8  
import sys, json, re
reload(sys)  
sys.setdefaultencoding('utf8')

if __name__ == "__main__":
    f = open("test_res.json")
    dict_main = json.load(f)
    f.close()
    n = len(dict_main)
    dict_res = []
    for i in range(n):
      dict_res.append(dict_main[i]['source_acronym_resolved'])         
    f = open("test_res_only_final.json", "w+")
    f.write(json.dumps(dict_res, sort_keys=True, indent=1, separators=(',', ': '), ensure_ascii=False))
    f.close()
