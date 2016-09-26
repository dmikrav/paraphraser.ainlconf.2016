f = open("data/all.txt")
all_data = f.readlines()
f.close()

all_data_key_value = []
for line in all_data:
  all_data_key_value.append(line.split("\t"))
f = open("data/distinct.txt")
distinct_data = f.read()
f.close()
distinct_data = distinct_data.split(" ")
total_cnt = len(distinct_data)
found_cnt = 0
absent_list = []
for w in distinct_data:
  flag = False
  for key_value in all_data_key_value:
    if key_value[0] == w:
      print w, "\t", key_value[1][:-1]
      flag = True
      found_cnt += 1
      break
  if not flag:
    absent_list.append(w)
    print w, "\t", "meaning for acronym not found"
print "\n", "Total found =", 100.0*found_cnt/total_cnt, "%"
print "\n", "Absent list:", "\n"
for w in absent_list:
  print w+"\t"

