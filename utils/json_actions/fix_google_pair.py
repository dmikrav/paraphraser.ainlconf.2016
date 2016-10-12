# -*- coding: utf-8 -*-
# encoding=utf8  
import sys, json, re
reload(sys)  
sys.setdefaultencoding('utf8')

if __name__ == "__main__":
    f = open("test_res.json")
    dict_main = json.load(f)
    f.close()
    n = len(list(dict_main))
    for i in range(n):
      tmp = dict_main[i]['translations']['google']
      dict_main[i]['translations']['google'] = {}
      dict_main[i]['translations']['google']['pair'] = tmp
    f = open("test_res_2.json", "w+")
    f.write(json.dumps(dict_main, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
    f.close()
