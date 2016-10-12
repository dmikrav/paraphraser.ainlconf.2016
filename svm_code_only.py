sys.path.append(os.path.abspath("./utils"))
from extract_ner_person_and_organization import get_ner_score as get_ner_score
import datetime
import time
import sklearn.ensemble 
# -*- coding: utf-8 -*-
# encoding=utf8  
import sys, json, re
reload(sys)  
sys.setdefaultencoding('utf8')
sm = difflib.SequenceMatcher(None)


ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print st
#print antonym_get_page.compute_opposite_list_flag(['rose', 'fall'])

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
    if (not os.path.exists("./json/"+str1md5+".json")):
	#raise ValueError("file not found: "+sentence_1)
        print "file not found: "+sentence_1
        flag = True
    if (not os.path.exists("./json/"+str2md5+".json")):
        #raise ValueError("file not found: "+sentence_1)
        print "file not found: "+sentence_2
        flag = True
    if flag:
      return ["", ""]
    with open("./json/"+str1md5+".json") as data_file:
  	sen = json.load(data_file)
	root1 = loadroot(sen)
    with open("./json/"+str2md5+".json") as data_file:
	sen = json.load(data_file)
        root2 = loadroot(sen)
    return [root1["lemma"], root2["lemma"], str1md5+".json", str2md5+".json", sentence_1, sentence_2]

#**********************************************************
def get_word_net_similarity(root):
  #print "@@", root[0], root[1]
  try: 
    if root == None or len(root) != 6:
      return [0.12, 1.4, 0.2] #, 0.0, 0.0] #, 0.0, 0.0, 0.0]
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
      return [0.12, 1.4, 0.2] #, 0.5, 0.5] #, 0.5, 0.5, 0.5]
    

    #print wn.synsets(root[0])
    s_1 = get_first_synset_part_of_speech('v', wn.synsets(root[0]))
    #print  wn.synsets(root[1])
    s_2 = get_first_synset_part_of_speech('v', wn.synsets(root[1]))
    res = [s_1.path_similarity(s_2),
           s_1.lch_similarity(s_2),
           s_1.wup_similarity(s_2)
           #s_1.res_similarity(s_2, brown_ic),
           #s_1.res_similarity(s_2, genesis_ic)
           #s_1.jcn_similarity(s_2, brown_ic),
           #s_1.jcn_similarity(s_2, genesis_ic),
           #s_1.lin_similarity(s_2, semcor_ic)
     ]
  except:
    #print len(root), root
    res = [0.12, 1.4, 0.2] #, 0.5, 0.5] #, 0.5, 0.5, 0.5]
  return res
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
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

def load_embeddings(fname):
    f = (line.split(" ",1)[1] for line in file(fname))
    vecs = np.loadtxt(f)
    words = [line.split(" ",1)[0] for line in file(fname)]
    return words,vecs

def dist(word1, word2):
    word1 = str(word1).lower()
    word2 = str(word2).lower()
    if (word1 in words and word2 in words):
    	return np.dot(vecs[words.index(word1)], vecs[words.index(word2)])
    else:
	return 0

def square(list):
  return [i ** 2 for i in list]

def self_print_line(x):
  f = open("svm_code_only.py")
  lines = f.readlines()
  f.close()
  print lines[x].replace("\n", "")

def get_libdiff_score(listt):
  #print "|" + str(listt) + "|"
  sm.set_seq2(listt[0])
  sm.set_seq1(listt[1])
  return sm.ratio()

import nltk
def only_verbs(text):
  tokens = nltk.word_tokenize(text)
  pos_tagged_tokens = nltk.pos_tag(tokens)
  #print pos_tagged_tokens
  res = " "
  for x in pos_tagged_tokens:
    if 'v' == x[1].lower()[0:1]:
      res += x[0] + " "
  return res

#clf = ensemble.RandomForestClassifier(n_estimators=20, max_features="auto")
#clf = SVC(C=100.0, kernel='rbf')
#clf = sklearn.ensemble.GradientBoostingRegressor(n_estimators=10, max_depth=1, learning_rate=1.0)
clf = sklearn.ensemble.GradientBoostingClassifier(n_estimators=100, max_depth=3)
#print self_print_line(160)
classes_names = ["NON-paraphrase", "Near-paraphrase", "Precise-paraphrase"]

with open('dataset.json') as data_file:    
  data = json.load(data_file)
with open('test.json') as data_file:    
  jtest = json.load(data_file)  

jtest_copy_task_1 = list(jtest)
jtest_filtered_task_1 = jtest_copy_task_1
jtest_copy_task_2 = list(jtest)
jtest_filtered_task_2 = jtest_copy_task_2 


data_copy_task_1 = list(data)
data_copy_task_2 = data_copy_task_1
dataset_filtered_task_1 = data_copy_task_1
dataset_filtered_task_2 = data_copy_task_2
#import random
#random.shuffle(dataset_filtered_task_1)
#random.shuffle(dataset_filtered_task_2)

#   ....  [running settings]   ....
sett = "dataset"
#sett = "test"
task_no = 2
verbose = True
print "sett =", sett, ";   task_no =", task_no
#   ....  [end of running settings]   ....

'''
#   .... [these lines of code is for testing specifical metric]  ....
f = open("rrr.txt")
rrr = int(f.read())
f.close()
f = open("rrr.txt", "w+")
f.write(str(rrr+1))
f.close()
print "      [ rrr =", rrr, " ]"
#   .... [end of these lines of code]  ....
'''

if task_no == 2:
  classes_ids = [[], []]
  for a in data_copy_task_2:
    if a["class"] == classes_names[2]:
      a["class"] = classes_names[1]
  print "ver 1, task 2"
  train = [
        # testing specifical metric:
        # [a["blue_metrics"].values()[rrr]]
    
          a["translations"]["google"]["dkpro"].values()[0:3] 
        + a["translations"]["google"]["dkpro"].values()[4:9]
        + a["translations"]["google"]["dkpro"].values()[10:15]

        + a["translations"]["microsoft"]["dkpro"].values()[0:3] 
        + a["translations"]["microsoft"]["dkpro"].values()[4:9]
        + a["translations"]["microsoft"]["dkpro"].values()[10:15]

        + a["translations"]["yandex"]["dkpro"].values()[0:3] 
        + a["translations"]["yandex"]["dkpro"].values()[4:9]
        + a["translations"]["yandex"]["dkpro"].values()[10:15]

        
        + a["translations"]["google"]["semilar"].values()
        + a["translations"]["microsoft"]["semilar"].values()
        + a["translations"]["yandex"]["semilar"].values()      

        + a["translations"]["google"]["difflib"]
        + a["translations"]["microsoft"]["difflib"]
        + a["translations"]["yandex"]["difflib"]

        + a["translations"]["google"]["nltk_wordnet"]
        + a["translations"]["microsoft"]["nltk_wordnet"]
        + a["translations"]["yandex"]["nltk_wordnet"]

        + [a["translations"]["google"]["swoogle"]]
        + [a["translations"]["microsoft"]["swoogle"]]
        + [a["translations"]["yandex"]["swoogle"]]



        #+ a["translations"]["google"]["blue_metrics"].values()[:-4]
        #+ a["translations"]["microsoft"]["blue_metrics"].values()[:-4]
        #+ a["translations"]["yandex"]["blue_metrics"].values()[:-4]

        #+ a["blue_metrics"].values()[:-4]



        #+ a["translations"]["google"]["handy_ner"].values()
        #+ a["translations"]["microsoft"]["handy_ner"].values()
        #+ a["translations"]["yandex"]["handy_ner"].values()  

        #+ a["translations"]["google"]["word_embedding"].values()
        #+ a["translations"]["microsoft"]["word_embedding"].values()
        #+ a["translations"]["yandex"]["word_embedding"].values()
        
        
        ##  a["translations"]["google"]["features"].values()
        ##+ a["translations"]["yandex"]["features"].values()
         
        ##+ get_ner_score(a["translations"]["yandex"]["pair"][0], 
        ##                a["translations"]["yandex"]["pair"][1])
        
        ##+ get_word_net_similarity(roots(a["translations"]["google"]["pair"][0], a["translations"]["google"]["pair"][1]))

        ##+ get_word_net_similarity(roots(a["translations"]["yandex"]["pair"][0], a["translations"]["yandex"]["pair"][1]))
        ##+ [a["translations"]["google"]["swoogle"]]
        ##+ [a["translations"]["yandex"]["swoogle"]]
        
        # + [a["translations"]["yandex"]["antonym_bit"]]
        # get_ner_score(a["translations"]["google"]["pair"][0], a["translations"]["google"]["pair"][1])
      
  for a in dataset_filtered_task_2]

  jtest_data = [
          a["translations"]["google"]["dkpro"].values()[0:3] 
        + a["translations"]["google"]["dkpro"].values()[4:9]
        + a["translations"]["google"]["dkpro"].values()[10:15]

        + a["translations"]["microsoft"]["dkpro"].values()[0:3] 
        + a["translations"]["microsoft"]["dkpro"].values()[4:9]
        + a["translations"]["microsoft"]["dkpro"].values()[10:15]

        + a["translations"]["yandex"]["dkpro"].values()[0:3] 
        + a["translations"]["yandex"]["dkpro"].values()[4:9]
        + a["translations"]["yandex"]["dkpro"].values()[10:15]

        
        + a["translations"]["google"]["semilar"].values()
        + a["translations"]["microsoft"]["semilar"].values()
        + a["translations"]["yandex"]["semilar"].values()

        + a["translations"]["google"]["difflib"]
        + a["translations"]["microsoft"]["difflib"]
        + a["translations"]["yandex"]["difflib"]

        + a["translations"]["google"]["nltk_wordnet"]
        + a["translations"]["microsoft"]["nltk_wordnet"]
        + a["translations"]["yandex"]["nltk_wordnet"]

        + [a["translations"]["google"]["swoogle"]]
        + [a["translations"]["microsoft"]["swoogle"]]
        + [a["translations"]["yandex"]["swoogle"]]


        #+ a["translations"]["google"]["blue_metrics"].values()[:-4]
        #+ a["translations"]["microsoft"]["blue_metrics"].values()[:-4]
        #+ a["translations"]["yandex"]["blue_metrics"].values()[:-4]

        #+ a["blue_metrics"].values()[:-4]


        #+ [a["translations"]["google"]["handy_ner"]["the_same_proper_nouns_percentage"]]
        #+ [a["translations"]["microsoft"]["handy_ner"]["the_same_proper_nouns_percentage"]]
        #+ [a["translations"]["yandex"]["handy_ner"]["the_same_proper_nouns_percentage"]]

        #+ a["translations"]["google"]["handy_ner"].values()
        #+ a["translations"]["microsoft"]["handy_ner"].values()
        #+ a["translations"]["yandex"]["handy_ner"].values()

        #+ [a["translations"]["google"]["word_embedding"]['dot_extrema']]
        #+ [a["translations"]["microsoft"]["word_embedding"]['dot_extrema']]
        #+ [a["translations"]["yandex"]["word_embedding"]['dot_extrema']]
        
        ##  a["translations"]["google"]["features"].values()
        ##+ a["translations"]["yandex"]["features"].values()
         
        ##+ get_ner_score(a["translations"]["yandex"]["pair"][0], 
        ##                a["translations"]["yandex"]["pair"][1])
        
        ##+ get_word_net_similarity(roots(a["translations"]["google"]["pair"][0], a["translations"]["google"]["pair"][1]))

        ##+ get_word_net_similarity(roots(a["translations"]["yandex"]["pair"][0], a["translations"]["yandex"]["pair"][1]))
        ##+ [a["translations"]["google"]["swoogle"]]
        ##+ [a["translations"]["yandex"]["swoogle"]]
        
        # + [a["translations"]["yandex"]["antonym_bit"]]
        # get_ner_score(a["translations"]["google"]["pair"][0], a["translations"]["google"]["pair"][1])
      
       for a in jtest_copy_task_2]

  classes_dataset = [a["class"] for a in dataset_filtered_task_2]
  if sett == "test":
    clf.fit(train, classes_dataset)
    predicted = clf.predict(jtest_data)
    
    for i in range(len(predicted)):    
      jtest[i]['predicted_class_task_2'] = predicted[i]

    f = open("test_with_predictions_task_2.json", "w+")
    f.write(json.dumps(jtest, indent=1, separators=(',', ': '), ensure_ascii=False, sort_keys=True))
    f.close()
  elif sett == "dataset":
    predicted = sklearn.cross_validation.cross_val_predict(clf, train, classes_dataset, cv=5, verbose=3)

    print "Accuracy:", metrics.accuracy_score(classes_dataset, predicted) 
    print "micro-F1:", metrics.f1_score(classes_dataset, predicted, average='micro', pos_label=None) 
    print "macro-F1:", metrics.f1_score(classes_dataset, predicted, average='macro', pos_label=None) 
    print metrics.confusion_matrix(classes_dataset, predicted)
  
  ts = time.time()
  st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
  print st

if task_no == 1:

    classes_dataset = [a["class"] for a in dataset_filtered_task_1]
  #if sett == "dataset":  
    print "ver 1, task 1"
    train = [
        # testing specifical metric:
        # [a["blue_metrics"].values()[rrr]]
        
        
          a["translations"]["google"]["dkpro"].values()[0:3] 
        + a["translations"]["google"]["dkpro"].values()[4:9]
        + a["translations"]["google"]["dkpro"].values()[10:15]

        + a["translations"]["microsoft"]["dkpro"].values()[0:3] 
        + a["translations"]["microsoft"]["dkpro"].values()[4:9]
        + a["translations"]["microsoft"]["dkpro"].values()[10:15]

        + a["translations"]["yandex"]["dkpro"].values()[0:3] 
        + a["translations"]["yandex"]["dkpro"].values()[4:9]
        + a["translations"]["yandex"]["dkpro"].values()[10:15]


        + a["translations"]["google"]["semilar"].values()
        + a["translations"]["microsoft"]["semilar"].values()
        + a["translations"]["yandex"]["semilar"].values()

        + a["translations"]["google"]["difflib"]
        + a["translations"]["microsoft"]["difflib"]
        + a["translations"]["yandex"]["difflib"]

        + a["translations"]["google"]["nltk_wordnet"]
        + a["translations"]["microsoft"]["nltk_wordnet"]
        + a["translations"]["yandex"]["nltk_wordnet"]

        + [a["translations"]["google"]["swoogle"]]
        + [a["translations"]["microsoft"]["swoogle"]]
        + [a["translations"]["yandex"]["swoogle"]]

        + a["blue_metrics"].values()[:-4]
        

        #+ a["translations"]["google"]["blue_metrics"].values()[:-4]
        #+ a["translations"]["microsoft"]["blue_metrics"].values()[:-4]
        #+ a["translations"]["yandex"]["blue_metrics"].values()[:-4]


        #+ [get_libdiff_score([only_verbs(a["translations"]["google"]['pair'][0]), 
        #                      only_verbs(a["translations"]["google"]['pair'][1])])]
        #+ [get_libdiff_score([only_verbs(a["translations"]["microsoft"]['pair'][0]), 
        #                      only_verbs(a["translations"]["microsoft"]['pair'][1])])]
        #+ [get_libdiff_score([only_verbs(a["translations"]["yandex"]['pair'][0]), 
        #                      only_verbs(a["translations"]["yandex"]['pair'][1])])]


        #+ [a["translations"]["google"]["handy_ner"]["the_same_proper_nouns_percentage"]]
        #+ [a["translations"]["microsoft"]["handy_ner"]["the_same_proper_nouns_percentage"]]
        #+ [a["translations"]["yandex"]["handy_ner"]["the_same_proper_nouns_percentage"]]

        #+ a["translations"]["google"]["handy_ner"].values()
        #+ a["translations"]["microsoft"]["handy_ner"].values()
        #+ a["translations"]["yandex"]["handy_ner"].values()

        #+ [a["translations"]["google"]["word_embedding"]['dot_extrema']]
        #+ [a["translations"]["microsoft"]["word_embedding"]['dot_extrema']]
        #+ [a["translations"]["yandex"]["word_embedding"]['dot_extrema']]
        
        ##  a["translations"]["google"]["features"].values()
        ##+ a["translations"]["yandex"]["features"].values()
         
        ##+ get_ner_score(a["translations"]["yandex"]["pair"][0], 
        ##                a["translations"]["yandex"]["pair"][1])
        
        ##+ get_word_net_similarity(roots(a["translations"]["google"]["pair"][0], a["translations"]["google"]["pair"][1]))

        ##+ get_word_net_similarity(roots(a["translations"]["yandex"]["pair"][0], a["translations"]["yandex"]["pair"][1]))
        ##+ [a["translations"]["google"]["swoogle"]]
        ##+ [a["translations"]["yandex"]["swoogle"]]
        
        # + [a["translations"]["yandex"]["antonym_bit"]]
        # get_ner_score(a["translations"]["google"]["pair"][0], a["translations"]["google"]["pair"][1])
      
       for a in dataset_filtered_task_1]
    
    jtest_data = [
          a["translations"]["google"]["dkpro"].values()[0:3] 
        + a["translations"]["google"]["dkpro"].values()[4:9]
        + a["translations"]["google"]["dkpro"].values()[10:15]

        + a["translations"]["microsoft"]["dkpro"].values()[0:3] 
        + a["translations"]["microsoft"]["dkpro"].values()[4:9]
        + a["translations"]["microsoft"]["dkpro"].values()[10:15]

        + a["translations"]["yandex"]["dkpro"].values()[0:3] 
        + a["translations"]["yandex"]["dkpro"].values()[4:9]
        + a["translations"]["yandex"]["dkpro"].values()[10:15]

        
        + a["translations"]["google"]["semilar"].values()
        + a["translations"]["microsoft"]["semilar"].values()
        + a["translations"]["yandex"]["semilar"].values()

        + a["translations"]["google"]["difflib"]
        + a["translations"]["microsoft"]["difflib"]
        + a["translations"]["yandex"]["difflib"]

        + a["translations"]["google"]["nltk_wordnet"]
        + a["translations"]["microsoft"]["nltk_wordnet"]
        + a["translations"]["yandex"]["nltk_wordnet"]

        + [a["translations"]["google"]["swoogle"]]
        + [a["translations"]["microsoft"]["swoogle"]]
        + [a["translations"]["yandex"]["swoogle"]]

        + a["blue_metrics"].values()[:-4]

        #+ [get_libdiff_score([only_verbs(a["translations"]["google"]['pair'][0]), 
        #                      only_verbs(a["translations"]["google"]['pair'][1])])]
        #+ [get_libdiff_score([only_verbs(a["translations"]["microsoft"]['pair'][0]), 
        #                      only_verbs(a["translations"]["microsoft"]['pair'][1])])]
        #+ [get_libdiff_score([only_verbs(a["translations"]["yandex"]['pair'][0]), 
        #                      only_verbs(a["translations"]["yandex"]['pair'][1])])]



        #+ [a["translations"]["google"]["handy_ner"]["the_same_proper_nouns_percentage"]]
        #+ [a["translations"]["microsoft"]["handy_ner"]["the_same_proper_nouns_percentage"]]
        #+ [a["translations"]["yandex"]["handy_ner"]["the_same_proper_nouns_percentage"]]

        #+ a["translations"]["google"]["handy_ner"].values()
        #+ a["translations"]["microsoft"]["handy_ner"].values()
        #+ a["translations"]["yandex"]["handy_ner"].values()

        #+ [a["translations"]["google"]["word_embedding"]['dot_extrema']]
        #+ [a["translations"]["microsoft"]["word_embedding"]['dot_extrema']]
        #+ [a["translations"]["yandex"]["word_embedding"]['dot_extrema']]
        
        ##  a["translations"]["google"]["features"].values()
        ##+ a["translations"]["yandex"]["features"].values()
         
        ##+ get_ner_score(a["translations"]["yandex"]["pair"][0], 
        ##                a["translations"]["yandex"]["pair"][1])
        
        ##+ get_word_net_similarity(roots(a["translations"]["google"]["pair"][0], a["translations"]["google"]["pair"][1]))

        ##+ get_word_net_similarity(roots(a["translations"]["yandex"]["pair"][0], a["translations"]["yandex"]["pair"][1]))
        ##+ [a["translations"]["google"]["swoogle"]]
        ##+ [a["translations"]["yandex"]["swoogle"]]
        
        # + [a["translations"]["yandex"]["antonym_bit"]]
        # get_ner_score(a["translations"]["google"]["pair"][0], a["translations"]["google"]["pair"][1])
      
    for a in jtest_copy_task_1]
    
    if sett == "dataset":   
      predicted = sklearn.cross_validation.cross_val_predict(clf, train, classes_dataset, cv=5, verbose=3)
      print "Accuracy:", metrics.accuracy_score(classes_dataset, predicted) 
      print "micro-F1:", metrics.f1_score(classes_dataset, predicted, average='micro', pos_label=None) 
      print "macro-F1:", metrics.f1_score(classes_dataset, predicted, average='macro', pos_label=None) 

      print metrics.confusion_matrix(classes_dataset, predicted)

    elif sett == "test":
      clf.fit(train, classes_dataset)
      predicted = clf.predict(jtest_data)
    
      for i in range(len(predicted)):    
        jtest[i]['predicted_class_task_1'] = predicted[i]

      f = open("test_with_predictions_task_1.json", "w+")
      f.write(json.dumps(jtest, indent=1, separators=(',', ': '), ensure_ascii=False), sort_keys=True)
      f.close()
    
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print st

   
    if verbose and sett == "dataset" and False:
      for i in range(len(predicted)):
        if predicted[i] != classes_dataset[i] and classes_dataset[i] == classes_names[2]:
          print "=" * 80
          print "predicted:" , predicted[i] , ";  actual:" , classes_dataset[i] 
          print "-" * 80
          print(dataset_filtered_task_1[i]["id"])
          print(dataset_filtered_task_1[i]["source"][0].encode('utf8'))
          print(dataset_filtered_task_1[i]["source"][1].encode('utf8'))

          pprint(dataset_filtered_task_1[i]["translations"]["google"]['pair'][0]) 
          pprint(dataset_filtered_task_1[i]["translations"]["google"]['pair'][1])

          pprint(only_verbs(dataset_filtered_task_1[i]["translations"]["google"]['pair'][0])) 
          pprint(only_verbs(dataset_filtered_task_1[i]["translations"]["google"]['pair'][1]))

          pprint(dataset_filtered_task_1[i]["translations"]["yandex"]['pair'][0]) 
          pprint(dataset_filtered_task_1[i]["translations"]["yandex"]['pair'][1])

          pprint(only_verbs(dataset_filtered_task_1[i]["translations"]["yandex"]['pair'][0])) 
          pprint(only_verbs(dataset_filtered_task_1[i]["translations"]["yandex"]['pair'][1]))


          print "\n"
  
