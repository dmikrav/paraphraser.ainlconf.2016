f = open("swoogle/yandex")
lines_swoogle = f.readlines()
f.close()
f = open("with_swoogle_0.json")
content_json = f.read()
f.close()
tagA = '            "yandex": {'
tagB = '                "features": {'

tag = '                "swoogle" : '

pos = 0
tmp = ''
for i in range(7227):
  pos = content_json.find(tagA, pos+len(tmp)+10)
  pos = content_json.find(tagB, pos)
  tmp = tag+str(float(lines_swoogle[i*4+2]))+',\n'
  content_json = content_json[0:pos] + tmp + content_json[pos:]

f = open("with_swoogle_1.json", "w+")
f.write(content_json)
f.close()

