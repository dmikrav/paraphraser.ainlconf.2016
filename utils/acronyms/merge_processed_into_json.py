# -*- coding: UTF-8 -*-
# encoding=utf8  
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')
from pprint import pprint

with open('data/out1.txt.bk') as data_file:    
  new_sentences = data_file.readlines()
print len(new_sentences), len(new_sentences)/3.0
with open('../../dataset.json') as data_file:    
  text = data_file.read()
tag_input = '        "translations": {'
tags_output = ['        "source_acronym_resolved": [', '            ', '        ],']
i = 0
length = 0
posA = 0
while True:
  posA = text.find(tag_input, posA + length)
  if posA == -1:
    break
  text = (text[:posA] + 
         tags_output[0] + '\n' +
         tags_output[1] + '"' + new_sentences[i*3].replace('\n', '') + '",' + '\n' + 
         tags_output[1] + '"' + new_sentences[i*3+1].replace('\n', '') + '"' + '\n' +
         tags_output[2] + '\n' +
         text[posA:])
  length = len(tags_output[0]) + len(tags_output[1]) + len(tags_output[2]) + 20 + len(new_sentences[i*3]) + len(new_sentences[i*3+1])
  i += 1
f = open("database_new.json", "w+")
f.write(text)
f.close()
