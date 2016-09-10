import json

with open('dataset.json') as data_file:    
  data = json.load(data_file)
  
data_copy = list(data)

train = [[a["translations"]["yandex"]["pair"][0], 
          a["translations"]["yandex"]["pair"][1]]
  for a in data_copy]

for i in range(10):
  print train[i][0]
  print train[i][1], '\n'
