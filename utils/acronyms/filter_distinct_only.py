f = open("data/11.txt")
data = f.read()
f.close()
listt = data.split(" ")
res = sorted(set(listt))
r = ""
for w in res:
  r = r + w + " "
print r
