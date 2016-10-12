import json
import codecs
# encoding=utf8  
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')
path_dir = "../../backup_data/"
main_dir = "../../"
xml = "clear_input.txt"
output = "test.json"
path_in = path_dir + xml
path_out = main_dir + output
f = open(path_in)
line = f.readlines()
f.close()
n = len(line)/3
res = []
for i in range(n):
  dict_tmp = {}
  # dict_tmp["source"] = [(line[i*3].replace("\n", "")).encode('utf8'), (line[i*3+1][:-1].replace("\n", "")).encode('utf8')]
  dict_tmp["source"] = [line[i*3][:-1], line[i*3+1][:-1]]
  tmp = str(i+1)
  dict_tmp["id"] = "99" + "0" * (7 - len(tmp) - 2) + tmp
  dict_tmp["real_class"] = 8 
  res.append(dict_tmp) 
'''
f = open(path_out, "w+")
f.write(json.dumps(res, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False).encode('utf8'))
f.close()
'''
s = json.dumps(res, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
file = codecs.open(path_out, "w+", "utf-8")
file.write(s)
#file.write(u'\ufeff')
file.close()
