# -*- coding: utf-8 -*-
# encoding=utf8  
import sys, json, re
reload(sys)  
sys.setdefaultencoding('utf8')

if __name__ == "__main__":
    f = open("misc/acronyms_resolved.txt")
    lines = f.readlines()
    f.close()
    f = open("../../test.json")
    jdata = json.load(f)
    f.close()
    n = len(lines)/3
    for i in range(n):
      jdata[i]['source_acronym_resolved'] = [lines[i*3].replace("\n", ""), lines[i*3+1].replace("\n", "")]
    f = open("test_res.json", "w+")
    f.write(json.dumps(jdata, sort_keys=True, indent=1, separators=(',', ': '), ensure_ascii=False))
    f.close()
