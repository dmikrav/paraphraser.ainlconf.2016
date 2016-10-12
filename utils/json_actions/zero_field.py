# -*- coding: utf-8 -*-
# encoding=utf8  
import sys, json, re
reload(sys)  
sys.setdefaultencoding('utf8')

if __name__ == "__main__":
    f = open("../../test.json")
    dict_main = json.load(f)
    f.close()
    n = len(dict_main)
    a = ['google', 'microsoft', 'yandex']
    for i in range(n):
      for x in range(3):
        dict_main[i]['translations'][a[x]]['dkpro'] = {}
    f = open("test.json", "w+")
    f.write(json.dumps(dict_main, sort_keys=True, indent=1, separators=(',', ': '), ensure_ascii=False))
    f.close()
