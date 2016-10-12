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
      tmp = dict_main[i]['source_acronym_resolved']
      sss = ["", ""]
      #for x in range(2): 
        #sss[x] = re.sub("[^абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯa-zA-Z .,:%;@0-9-]", "", tmp[x].encode('utf8'))
      dict_main[i]['source_acronym_resolved_final'] = [tmp[0], tmp[1]]
    f = open("dataset_res.json", "w+")
    f.write(json.dumps(dict_main, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
    f.close()
