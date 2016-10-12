# -*- coding: utf-8 -*-
# encoding=utf8  
import sys, json, re
reload(sys)  
sys.setdefaultencoding('utf8')
import json
f = open("../../test.json")
jdata = json.load(f)
f.close()
n = len(jdata)
print n


a = ["google", "microsoft", "yandex"]
#b = ["WordNGramJaccardMeasure", "CosineSimilarity", "LevenshteinComparator", "WordNGramContainmentMeasure"]
b = ["WordNGramJaccardMeasure_2", "WordNGramJaccardMeasure_3", "WordNGramJaccardMeasure_4", "WordNGramContainmentMeasure", "CosineSimilarity", "WordNGramContainmentMeasure", "ExactStringMatchComparator", "SubstringMatchComparator", "GreedyStringTiling_2", "GreedyStringTiling_3", "GreedyStringTiling_4", "JaroSecondStringComparator", "JaroWinklerSecondStringComparator", "MongeElkanSecondStringComparator", "LongestCommonSubsequenceNormComparator","LevenshteinComparator"]
len_b = len(b)

for x in range(3):
  f = open("dkpro_res_data_extracted_translations_train_set/extracted_" + a[x] + ".txt")
  lines = f.readlines()
  f.close()
  for i in range(n):
    jdata[i]['translations'][a[x]]['dkpro'] = {}
    tmp = lines[i*4+3].replace("\n", "").split(",")
    for z in range(len_b):
      jdata[i]['translations'][a[x]]['dkpro'][b[z]] = tmp[z]
f = open("test.json", "w+")
f.write(json.dumps(jdata, sort_keys=True, indent=1, separators=(',', ': '), ensure_ascii=False))
f.close()
