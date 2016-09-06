import hashlib
import json, sys
import os, os.path


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
      d[i[0]].append(i[1])
    else:
      d[i[0]].append(i[1])
  return d
    

def output_ner(string1, string2):
  #dir_path_to_ner = "write/here/the/path/"
  #dir_path_to_ner = "../intermediate_data/json"
  dir_path_to_ner = "/home/user/000/json"
  str1md5 = hashlib.md5(string1).hexdigest()
  str2md5 = hashlib.md5(string2).hexdigest()
  filename_INput = [dir_path_to_ner + "/" + str1md5+".json", dir_path_to_ner + "/" + str2md5 + ".json"]
  flag = False
  if (not os.path.exists(filename_INput[0])):
    print "file not found: "+string1 + " ;  " + str1md5  
    flag = True     
  #  raise ValueError("file not found: "+string1)
  if (not os.path.exists(filename_INput[1])):
    print "file not found: "+string2 + " ;  " + str2md5       
    flag = True
  if flag:
    return
  #  raise ValueError("file not found: "+string2)
  #hash_table = [[], []]
  res = ['', '']
  for i in range(2):
    js = open(filename_INput[i])
    data = json.load(js);
    js.close()
    s = process_sentence(data)
    res[i] = s
  return res[0], res[1]

# usage:
# output_ner("First sentence content", "Second sentence content")
s0, s1 = output_ner("Returning from Syria Russians are concerned about employment in their homeland.", "Emergencies Ministry aircraft will take out the Russians from Syria destroyed. ")
print s0
print s1
s0, s1 = output_ner("In Saratov brawler from the airplane Moscow - Hurghada opened a case.", "Saratov rowdy refuses to return home from Egypt. ")
print s0
print s1
s0, s1 = output_ner("Court of St. Petersburg on the left then the case of the death of a teenager in police custody.", "London Hyde Park - this is not a place for meetings, but primarily park. ")
print s0
print s1
s0, s1 = output_ner("OPEC has cut oil production by 1 million barrels a day.", "Obama has extended the powers of NASA's cooperation with Russia.")
print s0
print s1
