import hashlib
import json, sys
import os, os.path
import inspect, os

from get_json_by_string import get_json

localdir =  os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) # script directory

def process_sentence(data):
  l = [[], []]
  l[0] = [[a['ner'], a['normalizedNER']] for a in data['sentences'][0]['tokens'] if 'normalizedNER' in a]
  l[1] = [[a['ner'], a['lemma']] for a in data['sentences'][0]['tokens'] if a['ner']!='O' and not ('normalizedNER' in a)]
  tmp = l[0] + l[1]
  d = {}
  for i in tmp:
    if not i[0] in d:
      d[i[0]] = []
    
    if i[1] not in d[i[0]]:   
      d[i[0]].append(i[1])
	
    d[i[0]].sort()
  return d
    

def output_ner(string1, string2):
  res = ["", ""]
  jsons = [get_json(string1), get_json(string2)]
  for i in range(2):
    s = process_sentence(jsons[i])
    res[i] = s
  return res[0], res[1]

def get_similarity_score(json1, json2):
  res_dict = {}
  all_keys = json1.keys() + json2.keys()
  for key in all_keys:
    vals1 = []
    vals2 = []
    if key in json1:
      vals1 = json1[key]
    if key in json2:
      vals2 = json2[key]
    tmp = vals1 + vals2
    values_quantity = len(list(set(tmp)))
    identical_quantity = 0
    for x1 in vals1:
      for x2 in vals2:
        if x1 == x2:
          identical_quantity += 1
    # res_dict[key] = float(identical_quantity*1.0)
    res_dict[key] = float(identical_quantity*1.0/values_quantity)

  return res_dict

def convert_to_list(score):
  print score
  score_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  params = {"DURATION": 0, "ORGANIZATION": 1, "LOCATION": 2, "NUMBER": 3, "PERSON": 4, "ORDINAL": 5, "PERCENT": 6, "MONEY":7, "DATE":8, "TIME":9, "SET":10}

  for k,v in score.items():
    if v==0: 
      v = -1
    score_list[params[str(k)]] = v

  summm = 0
  for a in score_list:
    summm += a

  score_list.append(summm)  
  print score_list
  return score_list

def get_ner_score(str1, str2):
  ner1,ner2 = output_ner(str1, str2)
  print ner1
  print ner2
  return convert_to_list(get_similarity_score(ner1, ner2))
#print __dir__
#print os.path.abspath(os.path.dirname(__file__))

# usage:
# output_ner("First sentence content", "Second sentence content")
a = [["Returning from Syria Russians are concerned about employment in their homeland.", "Emergencies Ministry aircraft will take out the Russians from Syria destroyed. "],

["In Saratov brawler from the airplane Moscow - Hurghada opened a case.", "Saratov rowdy refuses to return home from Egypt. "],

["Court of St. Petersburg on the left then the case of the death of a teenager in police custody.", "London Hyde Park - this is not a place for meetings, but primarily park. "],

["OPEC has cut oil production by 1 million barrels a day.", "Obama has extended the powers of NASA's cooperation with Russia."]]
for i in a:
  res1, res2 = output_ner(i[0], i[1])
  print res1, "\n", res2
  print convert_to_list(get_similarity_score(res1, res2)), "\n" + "*" * 80



# print convert_to_list(get_similarity_score({"loc":["paris", "moscow", "berlin"], "per":["dima"]}, {"loc":["paris", "berlin", "chita"], "per":["dima", "egor"]}))
