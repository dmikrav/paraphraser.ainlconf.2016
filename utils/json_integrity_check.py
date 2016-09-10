import json



with open('../dataset.json') as data_file:    
  data = json.load(data_file)
  
data_copy = list(data)

arr_from_json = [
  [a["translations"]["yandex"]["pair"][0], 
  a["translations"]["yandex"]["pair"][1]]
    for a in data_copy]

f = open("../intermediate_data/yandex_translate/analysis_yandex_")
lines = f.readlines()
f.close()

n = len(lines)/10

arr_from_file = [
  [lines[i*10][11:], lines[i*10][11:]]
    for i in range(n)]
cnt = 0
for i in range(7227):
  if arr_from_json[i][0][:10] != arr_from_file[i][0][:10]:# or 
  #if arr_from_json[i][1] != arr_from_file[i][1]:
    cnt += 1
    if cnt<10:
#      print arr_from_json[i][0], '\n', arr_from_file[i][0], '\n'
      print arr_from_json[i][0], '\n', arr_from_file[i][0], '\n'

print "\ntotal:", cnt, '\n'
