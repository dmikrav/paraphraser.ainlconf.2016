# -*- coding: utf-8 -*-
# encoding=utf8  
import sys, json, re
reload(sys)  
sys.setdefaultencoding('utf8')

if __name__ == "__main__":
    f = open("dataset_res.json")
    dict_main = json.load(f)
    f.close()
    n = len(dict_main)
    for i in range(n):
      dict_main[i]['source_acronym_resolved'] = [dict_main[i]['source_acronym_resolved'][0].replace(" \n", ""), dict_main[i]['source_acronym_resolved'][1].replace(" \n", "")]
    f = open("dataset_res.json", "w+")
    f.write(json.dumps(dict_main, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
    f.close()
