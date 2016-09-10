import sys
import os.path
from sklearn.svm import SVC
from sklearn import ensemble
from sklearn import cross_validation
import sklearn
from sklearn import metrics
import json
from pprint import pprint
import random
import numpy as np
import hashlib
from numpy import linalg as la
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
from nltk.corpus import genesis

brown_ic = wordnet_ic.ic('ic-brown.dat')
semcor_ic = wordnet_ic.ic('ic-semcor.dat')
genesis_ic = wn.ic(genesis, False, 0.0)

sys.path.append(os.path.abspath("./utils"))
from extract_ner_person_and_organization import get_ner_score as get_ner_score

class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

#print hashlib.md5(" In Kazakhstan there are no such problems, but in Russia.").hexdigest()
#sys.exit(0)
#print  ner("Returning from Syria Russians are concerned about employment in their homeland.", "Emergencies Ministry aircraft will take out the Russians from Syria destroyed. ")

# return the ROOT token
def loadroot(sen):
   for token in sen["sentences"][0]["basic-dependencies"]:
   	if (token["dep"] == "ROOT"):
		return sen["sentences"][0]["tokens"][int(token["dependent"])-1]

# input: two strings
# output: the cosine distance between them
def rootdist(string1, string2):
    str1md5 = hashlib.md5(string1).hexdigest()
    str2md5 = hashlib.md5(string2).hexdigest()
	  
    if (not os.path.exists("./json/"+str1md5+".json")):
	raise ValueError("file not found: "+string1)

    if (not os.path.exists("./json/"+str2md5+".json")):
        raise ValueError("file not found: "+string2)

    with open("./json/"+str1md5+".json") as data_file:
  	sen = json.load(data_file)
	root1 = loadroot(sen)
    with open("./json/"+str2md5+".json") as data_file:
	sen = json.load(data_file)
        root2 = loadroot(sen)
    return dist(root1["lemma"], root2["lemma"])

# ========================================================
def roots(sentence_1, sentence_2):
    str1md5 = hashlib.md5(sentence_1).hexdigest()
    str2md5 = hashlib.md5(sentence_2).hexdigest()
    flag = False
    if (not os.path.exists("../json/"+str1md5+".json")):
	#raise ValueError("file not found: "+sentence_1)
        print "file not found: "+sentence_1
        flag = True
    if (not os.path.exists("../json/"+str2md5+".json")):
        #raise ValueError("file not found: "+sentence_1)
        print "file not found: "+sentence_2
        flag = True
    if flag:
      return ["", ""]
    with open("../json/"+str1md5+".json") as data_file:
  	sen = json.load(data_file)
	root1 = loadroot(sen)
    with open("../json/"+str2md5+".json") as data_file:
	sen = json.load(data_file)
        root2 = loadroot(sen)
    return [root1["lemma"], root2["lemma"], str1md5+".json", str2md5+".json", sentence_1, sentence_2]

#**********************************************************
def get_word_net_similarity(root):
  print "@@", root[0], root[1]
  try: 
    if root == None or len(root) != 6:
      return [0, 0]
    flag = False
    if len(wn.synsets(root[0])) == 0 or not is_there_part_of_speech('v', wn.synsets(root[0])):
      #print root[0]+';   ', root[4], '   ', root[2] 
      root = ['place', root[1]]
      flag = True
    if len(wn.synsets(root[1])) == 0 or not is_there_part_of_speech('v', wn.synsets(root[1])):
      #print root[1]+';   ', root[5], '   ',root[3]
      root = [root[0], 'place']
      flag = True
    if flag:
      #print "-" * 80
      return [0.5, 0.5]
    

    #print wn.synsets(root[0])
    s_1 = get_first_synset_part_of_speech('v', wn.synsets(root[0]))
    #print  wn.synsets(root[1])
    s_2 = get_first_synset_part_of_speech('v', wn.synsets(root[1]))
    res = [s_1.path_similarity(s_2),
           s_1.lch_similarity(s_2),
           s_1.wup_similarity(s_2),
           s_1.res_similarity(s_2, brown_ic),
           s_1.res_similarity(s_2, genesis_ic),
           s_1.jcn_similarity(s_2, brown_ic),
           s_1.jcn_similarity(s_2, genesis_ic),
           s_1.lin_similarity(s_2, semcor_ic)
     ]
  except:
    #print len(root), root
    res = [0.5, 0.5]
  return res
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def get_relevant_wordnet_synsets(root):
  flag = False
  if len(wn.synsets(root[0])) == 0:
    #print root[0]
    root = ['place', root[1]]
    flag = True
  if len(wn.synsets(root[1])) == 0:
    #print root[1]
    root = [root[0], 'place']
    flag = True
  if flag:
    pass
    #print "-" * 20
  s_1 = wn.synsets(root[0])[0]
  s_2 = wn.synsets(root[1])[0]
  #part_of_speech_1 = 
#---------------------------------------------------------
def get_part_of_speech(s):
  part_of_speech = ['v', 'n', 'a', 's']
  n = len(part_of_speech)
  for x in range(n):
    if s.find('.'+part_of_speech[i]+'.') != -1:
      return part_of_speech[i]
  return ''
#---------------------------------------------------------
def is_there_part_of_speech(part_of_speech, synsets):
  n = len(synsets)
  for i in range(n):
    s = str(synsets[i])
    if s.find('.'+part_of_speech+'.') != -1:
      return True
  return False
#---------------------------------------------------------
def get_first_synset_part_of_speech(part_of_speech, synsets):
  n = len(synsets)
  for i in range(n):
    s = str(synsets[i])
    if s.find('.'+part_of_speech+'.') != -1:
      return synsets[i]
  return None
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

with open('../dataset.json') as data_file:    
  data = json.load(data_file)
  
data_copy = list(data)
dataset_filtered = data_copy 
train = [[a["translations"]["yandex"]["pair"][0], 
          a["translations"]["yandex"]["pair"][1]]
        # get_ner_score(a["translations"]["google"]["pair"][0], a["translations"]["google"]["pair"][1])
  for a in dataset_filtered]

for x in range(7227):
  t = roots(train[x][0], train[x][1])
  if t[0] == "" or t[1] == "":
    continue
  print get_word_net_similarity(t)
#print get_word_net_similarity(train[0])
#root_1, root_2 = roots(train[0][0], train[0][1])
#print get_word_net_similarity(root_1, root_2)
