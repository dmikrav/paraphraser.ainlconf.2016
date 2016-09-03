import sys
import os.path
from sklearn.svm import SVC
from sklearn import ensemble
from sklearn import cross_validation
from sklearn import metrics
import json
from pprint import pprint


dir_name = "full_en_semilar_output"
indexes = ["-1", "0", "1"]

# clf = ensemble.RandomForestClassifier(n_estimators=20, max_features="auto")
clf = SVC(C=20.0, kernel='rbf')

# with open('example.json') as data_file:    
#   data = json.load(data_file)
  # pprint(data)


# print data[0]["source"][0]
# sys.exit()


train_text = []
train_float = []
classes = []
lll = []
for i in range(3):
  full_file_name = os.path.join(dir_name, indexes[i])
  f = open(full_file_name, "r")
  train_text.append(f.read())
  f.close()

for i in range(3):
  train_lines = train_text[i].split("\n")
  tmp_train_float = []
  tmp_classes = []
  for train_str in train_lines:
    tmp = []
    flag = False
    for y in train_str.split(","):
      if len(y) > 0:
        flag = True
        tmp.append(float(y))
    if flag: 
      tmp_train_float.append(tmp)
      tmp_classes.append(int(indexes[i]))
      if i == 2:
        lll.append(0)
  train_float.append(tmp_train_float)
  classes.append(tmp_classes)


data_set = []
classes_set = []
print "=" * 80
for task_no in range(2):
  print "\n    Task  {"+str(task_no+1)+"}"
  if task_no == 0:
    data_set = train_float[0] + train_float[1] + train_float[2]
    classes_set = classes[0] + classes[1] + lll
  if task_no == 1:
    data_set = train_float[1] + train_float[2]
    classes_set = classes[1] + classes[2]
  predicted = cross_validation.cross_val_predict(clf, data_set, classes_set, cv=5, verbose=3)
  print "Accuracy:", metrics.accuracy_score(classes_set, predicted) 
  print "micro-F1:", metrics.f1_score(classes_set, predicted, average='micro', pos_label=None) 
  print "macro-F1:", metrics.f1_score(classes_set, predicted, average='macro', pos_label=None) 
print "\n" + "=" * 80


