# -*- coding: utf-8 -*-
# encoding=utf8  
import sys, json, re
reload(sys)  
sys.setdefaultencoding('utf8')
import json
import re

def summ(res, v):
  for i in range(100):
    res[i] += v[i]

# calculate the distance between two paraphrase vectors
def dist(vector1, vector2):
  return np.dot(vector1, vector2)
n = len(words)

# return the vector of the paraphrase as a average of the word's vector   
def vectorstring_and_extrema(string):
  #print string
  string = re.sub('[^a-zA-Z0-9- ]', '', string)
  sentence = string.lower().split(" ")
  #print sentence
  res = [0] * 100
  cnt = 0
  not_started = True
  for w in sentence:
    for i in range(n):
      if words[i] == w:
        if not_started:
          not_started = False
          extr_acc = vecs[i]
        else:
          extr_acc = extrema(extr_acc, vecs[i]) 
        summ(res, vecs[i])
        cnt += 1
        break
  for i in range(100):
    res[i] = res[i] / cnt
  norms_extr_acc = la.norm(extr_acc)#, axis=1)
  nvecs = extr_acc / norms_extr_acc#[:,np.newaxis]
  extr_acc = nvecs
  #print extr_acc
  return res, extr_acc

def extrema(a, b):
  res = []
  for i in range(100):
    mn = min(a[i], b[i])
    mx = max(a[i], b[i])
    if mx >= abs(mn):
      res.append(mx)
    else:
      res.append(mn) 
  return res


f = open("../../dataset.json")
jdata = json.load(f)
f.close()
k = len(jdata)
ss = ["google", "microsoft", "yandex"]
for i in range(k):
  if i % 3 == 0:
    print i
  for x in range(3):
    listt = jdata[i]['translations'][ss[x]]['pair']
    vec_0, extr_acc_0 = vectorstring_and_extrema(listt[0])
    vec_1, extr_acc_1 = vectorstring_and_extrema(listt[1])
    jdata[i]['translations'][ss[x]]['word_embedding'] = {}
    jdata[i]['translations'][ss[x]]['word_embedding']['dot_distance'] = dist(vec_0, vec_1)
    jdata[i]['translations'][ss[x]]['word_embedding']['dot_extrema'] = dist(extr_acc_0, extr_acc_1)
    #jdata[i]['translations'][ss[x]]['word_embedding']['extrema'] = [extr_acc_0, extr_acc_1]
f = open("dataset_embed.json", "w+") 
f.write(json.dumps(jdata, sort_keys=True, indent=1, separators=(',', ': '), ensure_ascii=False))
f.close()
