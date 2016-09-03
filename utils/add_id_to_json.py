f = open("../dataset.json")
content_json = f.read()
f.close()
tagA = '        "source": ['
tag  = '        "id" : '


def with_padding(cnt):
  s = str(cnt)
  return '0'*(7-len(s))+s

pos = 0
tmp = ''
cnt = 1
for i in range(7227):
  pos = content_json.find(tagA, pos+len(tmp)+1)
  tmp = tag + '"' + with_padding(cnt) + '",\n'
  content_json = content_json[0:pos] + tmp + content_json[pos:]
  cnt += 1
f = open("../dataset_2.json", "w+")
f.write(content_json)
f.close()

