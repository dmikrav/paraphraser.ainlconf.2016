import json
f = open("../dataset.json")
jdata = json.load(f)
f.close()
res = []
brands = ['google', 'microsoft', 'yandex']
n = len(jdata)
m = len(brands)
for x in range(n):
  for y in range(m):
    a = jdata[x]['translations'][brands[y]]['swoogle']
    if a < 0:
      print a, jdata[x]['id'] 
