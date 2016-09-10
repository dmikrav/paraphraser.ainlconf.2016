
tags = '    {\n' +  '        "id" : "000'
tags_end = (
'                }\n' +
'            }\n' +
'        }\n' +
'    }')

classs = ['        "class": "NON-paraphrase",', 
          '        "class": "Near-paraphrase",',
          '        "class": "Precise-paraphrase",']

f = open("../dataset.json")
js = f.read()
f.close()
n = len(lines)
cla = [[], [], []]

posA = 0
while (posA != -1):
  posA = js.find(tags, posA+1)
  posA_end = js.find(tags_end, posA)
  pos_class = 0
  curr_class = -77
  while (pos_class == -1 and curr_class < 3):
    pos_class = js.find(classs[cnt], posA, posA_end)
    curr_class += 1
    if curr_class == -1:
      continue
    cla[curr_class].append()

f = open("../intermediate_data/dataset_78.json", "w+")
f.write(res78)
f.close()
f = open("../intermediate_data/dataset_18.json", "w+")
f.write(res18)
f.close()
