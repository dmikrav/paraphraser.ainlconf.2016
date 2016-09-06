import sys
import os.path
from sklearn.svm import SVC
from sklearn import ensemble
from sklearn import cross_validation
from sklearn import metrics
import json
from pprint import pprint
import random

# clf = ensemble.RandomForestClassifier(n_estimators=20, max_features="auto")
clf = SVC(C=20.0, kernel='rbf')

with open('merged.json') as data_file:    
  data = json.load(data_file)
  
data_copy = list(data)

random.shuffle(data_copy)
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

train = [a["translations"]["google"]["features"].values() for a in dataset_filtered]
classes = [a["class"] for a in dataset_filtered]

#scores = cross_validation.cross_val_score(clf, train_float[0] + train_float[1], classes[0] + classes[1], cv=10)
predicted = cross_validation.cross_val_predict(clf, train, classes, cv=5, verbose=3)

print "Accuracy:", metrics.accuracy_score(classes, predicted) 
print "micro-F1:", metrics.f1_score(classes, predicted, average='micro', pos_label=None) 
print "macro-F1:", metrics.f1_score(classes, predicted, average='macro', pos_label=None) 

google_translated = [a["translations"]["google"]["pair"] for a in dataset_filtered]
cnt = 0
for i in range(len(predicted)):
  if predicted[i] != classes[i]:
    print "predicted:", predicted[i], ";  actual:", classes[i], "\n", google_translated[i][0], "\n", google_translated[i][1], "\n"
    cnt += 1
print "\nTotal errors: "+str(cnt) + "\n"