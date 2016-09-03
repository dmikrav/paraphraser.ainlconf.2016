import json
from pprint import pprint
import string
printable = set(string.printable)

with open('dataset.json') as data_file:    
  data = json.load(data_file)

data_copy = list(data)

brands = ["google", "yandex"]
translation_content = [[a["translations"][brands[0]]["pair"] for a in data_copy],
                       [a["translations"][brands[1]]["pair"] for a in data_copy]]
n = 7227
for x in range(2):
  tmp = ""
  for i in range(n):
    tmp += filter(lambda x: x in printable, translation_content[x][i][0]) + '\n'
    tmp += filter(lambda x: x in printable, translation_content[x][i][1]) + '\n'
    tmp += "====================================" + '\n'
  f = open("translations_without_shared_words/all_"+brands[x] ,"w+")
  f.write(tmp)
  f.close()
