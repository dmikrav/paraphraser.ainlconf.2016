f = open("antonym_bit.txt")
lines = f.readlines()
f.close()
f = open("../dataset.json")
js = f.read()
f.close()
n = len(lines)
tag = '            "yandex": {\n'
insert = '                "antonym_bit" : '
pos = 0
print n
bits = []
for i in range(n):
  [x, y] = lines[i].split(" ")
  bits.append(str(int(y)))
for i in range(7227):
  pos = js.find(tag, pos+len(insert)+10)
  tmp = insert + bits[i] + ',\n'
  js = js[0:pos+len(tag)] + tmp + js[pos+len(tag):]
f = open("../dataset_2.json", "w+")
f.write(js)
f.close()

