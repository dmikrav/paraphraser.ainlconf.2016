# -*- coding: UTF-8 -*-
# encoding=utf8  
import sys, json  
reload(sys)  
sys.setdefaultencoding('utf8')
from pprint import pprint
import re

def is_proper(s):
  return len(filter(lambda x: (x>='A' and x<='Z'), s)) == 1

def get_ner(s):
  t = filter(lambda x: (x>='A' and x<='Z') or (x>='a' and x<='z') or x == ' ', s)
  lt = t.split(" ")
  lt[0] = lt[0].lower() 
  ner_all = [w for w in lt if is_proper(w)]
  return list(set(ner_all))

def primitive_ner_distance(ner1, ner2):
  values_quantity = len(list(set(ner1+ner2)))
  identical_quantity = 0
  for w1 in ner1:
    for w2 in ner2:
      if w1 == w2:
        identical_quantity += 1
  
  if (values_quantity == 0):
    return 1
  
  return float(identical_quantity*1.0/values_quantity)

ner1 = get_ner("All Pakistan crashed helicopter with 11 foreigners Lenin Lenin")
ner2 = get_ner("All Afgan crashed helicopter with 11 foreigners Lenin")

print ner1
print ner2

print primitive_ner_distance(ner1, ner2)