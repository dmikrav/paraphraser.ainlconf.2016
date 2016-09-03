import json
from pprint import pprint
import string
printable = set(string.printable)

with open('merged_yandex.json') as data_file:    
  data = json.load(data_file)
  
data_copy = list(data)

yandex = [a["translations"]["yandex"]["pair"] for a in data_copy]
n = len(yandex)
for i in range(n):
  print filter(lambda x: x in printable, yandex[i][0])
  print filter(lambda x: x in printable, yandex[i][1])
  print "===================================="
