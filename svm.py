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

sys.path.append(os.path.abspath("./utils"))
from extract_ner_person_and_organization import output_ner as ner

#print  ner("Returning from Syria Russians are concerned about employment in their homeland.", "Emergencies Ministry aircraft will take out the Russians from Syria destroyed. ")

sys.exit(0)

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

# clf = ensemble.RandomForestClassifier(n_estimators=20, max_features="auto")
clf = SVC(C=50.0, kernel='rbf')
#words,vecs = load_embeddings("./bow10.words")

#norms = la.norm(vecs, axis=1)
#nvecs = vecs / norms[:,np.newaxis]
#vecs = nvecs

with open('dataset.json') as data_file:    
  data = json.load(data_file)
  
data_copy = list(data)

#random.shuffle(data_copy)
print len(data_copy)

print "NON-paraphrase"
print len([a for a in data_copy if a["class"] == "NON-paraphrase"])

print "Precise-paraphrase"
print len([a for a in data_copy if a["class"] == "Precise-paraphrase"])

print "Near-paraphrase"
print len([a for a in data_copy if a["class"] == "Near-paraphrase"])

# filter new paraphrases
dataset_filtered = [a for a in data_copy if (a["class"] == "NON-paraphrase" or a["class"] == "Precise-paraphrase")]
print len(dataset_filtered)

#train = [a["translations"]["google"]["features"].values()+square(a["translations"]["google"]["features"].values()) for a in dataset_filtered]
#train = [a["translations"]["google"]["features"].values() for a in dataset_filtered]
train = [a["translations"]["google"]["features"].values()+a["translations"]["yandex"]["features"].values() for a in dataset_filtered]
#train = [a["translations"]["google"]["features"].values()+a["translations"]["yandex"]["features"].values()+[rootdist(a["translations"]["yandex"]["pair"][0], a["translations"]["yandex"]["pair"][1])] for a in dataset_filtered]
#train = [a["translations"]["yandex"]["features"].values() for a in dataset_filtered]

#print train

classes = [a["class"] for a in dataset_filtered]

#scores = cross_validation.cross_val_score(clf, train_float[0] + train_float[1], classes[0] + classes[1], cv=10)
predicted = sklearn.cross_validation.cross_val_predict(clf, train, classes, cv=5, verbose=3)

print "Accuracy:", metrics.accuracy_score(classes, predicted) 
print "micro-F1:", metrics.f1_score(classes, predicted, average='micro', pos_label=None) 
print "macro-F1:", metrics.f1_score(classes, predicted, average='macro', pos_label=None) 

print metrics.confusion_matrix(classes, predicted)

google_translated = [a["translations"]["google"]["pair"] for a in dataset_filtered]
for i in range(len(predicted)):
  if predicted[i] != classes[i]:
    print "predicted:" , predicted[i] , ";  actual:" , classes[i] , "\n" 
    
    print(dataset_filtered[i]["source"][0].encode('utf8'))
    print(dataset_filtered[i]["source"][1].encode('utf8'))
    pprint(dataset_filtered[i]["translations"]["google"]) 
    pprint(dataset_filtered[i]["translations"]["yandex"])
    print "\n"
