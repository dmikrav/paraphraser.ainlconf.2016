import hashlib
import json, sys
import os, os.path

def push(hash_table, key, value):
  n = len(hash_table)
  for i in range(n):
    if key == hash_table[i][0]:
      hash_table[i].append(value)
      return
  hash_table.append([key, value])

def to_string(hash_table):
  res = '{\n'
  n = len(hash_table)
  for r in range(n):
    res += '  "' + hash_table[r][0] + '" : [' 
    m = len(hash_table[r])
    for c in range(1, m):
      psik_or_not = ','
      if c == m-1:
        psik_or_not = ''
      res += '"' + hash_table[r][c] + '"' + psik_or_not
    psik_or_not = ',' 
    if r == n-1:
      psik_or_not = ''
    res += ']' + psik_or_not + '\n'
  res += '}'
  return res

def extract_value(s):
  posA = s.find('"')
  posB = s.rfind('"')
  return s[posA+1:posB]

def process_sentence(hash_table, lst):
  pattern = [['normalizedNER'], ['"ner":']] 
  auxiliary = [['ner'], ['lemma']]
  n = len(lst)
  for i in range(n):
    for patt_no in range(2):
      for patt_no_iteration in range(len(pattern[patt_no])):
        pos1 = lst[i].find(pattern[patt_no][patt_no_iteration])
        if (pos1 != -1):
          s0 = ''
          s1 = ''
          if patt_no == 0:
            pos0 = lst[i-1].find(auxiliary[patt_no][patt_no_iteration])
            s0 = extract_value(lst[i-1][pos0+len(auxiliary[patt_no][patt_no_iteration])+1:])
            s1 = extract_value(lst[i][pos1+len(pattern[patt_no][patt_no_iteration])+1:])
            push(hash_table, s0, s1)
          if patt_no == 1 and lst[i].find('ner": "O",') == -1 and lst[i+1].find("normalizedNER") == -1:
            pos0 = lst[i-4].find(auxiliary[patt_no][patt_no_iteration])
            tmp = '"ner": '
            pos1 = lst[i].find(tmp)+len(tmp)
            s0 = extract_value(lst[i-4][pos0+len(auxiliary[patt_no][patt_no_iteration])+1:])
            s1 = extract_value(lst[i][pos1:])
            push(hash_table, s1, s0)
  return to_string(hash_table)

def output_ner(string1, string2): 
  str1md5 = hashlib.md5(string1).hexdigest()
  str2md5 = hashlib.md5(string2).hexdigest()
  filename_INput = ["../intermediate_data/json/"+str1md5+".json", "../intermediate_data/json/"+str2md5+".json"]
  filename_OUTput = ["../intermediate_data/json_ner_output/"+str1md5+".json", "../intermediate_data/json_ner_output/"+str2md5+".json"]
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
  hash_table = [[], []]
  for i in range(2):
    f = open(filename_INput[i])
    lst = f.readlines();
    f.close()
    s = process_sentence(hash_table[i], lst)
    f = open(filename_OUTput[i], "w+")
    f.write(s);
    f.close()


#with open('../backup_data/dataset_test_short.json') as data_file:
with open('../dataset.json') as data_file:    
  data = json.load(data_file)
data_copy = list(data)
dataset_filtered = data_copy #[a for a in data_copy if (a["class"] == "NON-paraphrase" or a["class"] == "Precise-paraphrase")]
google_translated = [a["translations"]["google"]["pair"] for a in dataset_filtered] + [a["translations"]["yandex"]["pair"] for a in dataset_filtered]
m = str(len(google_translated))
cnt = 0
for i in google_translated:
  #sys.stdout.write(str(cnt) + " of " + m + "\n")
  #sys.stdout.flush()
  output_ner(i[0], i[1])
  cnt += 1


