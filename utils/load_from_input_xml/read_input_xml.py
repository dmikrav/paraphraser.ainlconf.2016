path_dir = "../../backup_data/"
xml = "paraphrases_test.xml"
output = "clear_input.txt"
path_in = path_dir + xml
path_out = path_dir + output
f = open(path_in)
line = f.readlines()
f.close()
n = len(line)
tags = ['<value name="text_1">', '<value name="text_2">', '</value>']
res = ""
cnt_flag = 0
for i in range(n):
  for x in range(2):
    if line[i].find(tags[x]) >= 0:
      posA = line[i].find(tags[x]) + len(tags[x])
      posB = line[i].find(tags[2])
      if posA < 0 or posB < 0:
        raise Exception("bad format "+ line[i])
      res += line[i][posA:posB] + "\n"
      cnt_flag += 1
  if cnt_flag >= 2:
    res += "===\n"
    cnt_flag = 0
f = open(path_out, "w+")
f.write(res)
f.close()
