import hashlib
import json, sys
import os, os.path
import inspect, os

from get_json_by_string import get_json

localdir =  os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) # script directory

def process_sentence(data):
  #l = [a for a in ss['sentences'][0]['tokens'] if 'normalizedNER' in a]
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

#print __dir__
#print os.path.abspath(os.path.dirname(__file__))

# usage:
# output_ner("First sentence content", "Second sentence content")
print output_ner("Returning from Syria Russians are concerned about employment in their homeland.", "Emergencies Ministry aircraft will take out the Russians from Syria destroyed. ")
print output_ner("In Saratov brawler from the airplane Moscow - Hurghada opened a case.", "Saratov rowdy refuses to return home from Egypt. ")
print  output_ner("Court of St. Petersburg on the left then the case of the death of a teenager in police custody.", "London Hyde Park - this is not a place for meetings, but primarily park. ")
print output_ner("OPEC has cut oil production by 1 million barrels a day.", "Obama has extended the powers of NASA's cooperation with Russia.")
