import string
printable = set(string.printable)

f = open("with_swoogle_1.json")
content_json = f.read()
f.close()

posA = 0
posB = 0
tmp = ''

tagA = '                "pair": ['
tagB = '                ],'

for i in range(7227*2):
  posA = content_json.find(tagA, posB+1)
  posB = content_json.find(tagB, posA)
  tmp = filter(lambda x: x in printable, content_json[posA:posB])
  content_json = content_json[0:posA] + tmp + content_json[posB:]

f = open("with_swoogle_1_clear.json", "w+")
f.write(content_json)
f.close()

