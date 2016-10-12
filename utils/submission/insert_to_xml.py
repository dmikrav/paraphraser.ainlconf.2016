# -*- coding: utf-8 -*-
# encoding=utf8  
import sys, json, re
reload(sys)  
sys.setdefaultencoding('utf8')
import json
f = open("../../test.json")
jtest = json.load(f)
f.close()
jtest = list(jtest)
for uu in range(2):
  task_no = 'task_' + str(uu+1) 
  listt = [a['predicted_class_' + task_no] for a in jtest]
  class_names = ["NON-paraphrase", "Near-paraphrase", "Precise-paraphrase"] 
  class_numbers = []
  if uu == 0:
    delta = -1
  elif uu == 1:
    delta = 0
  for i in range(1924):
    for x in range(3):
      if listt[i] == class_names[x]:
        class_numbers.append(x+delta)
  print len(class_numbers)
  f = open("paraphrases_test.xml") 
  xml = f.read()
  f.close()
  tags_in = ['<value name="text_2">', '</value>\n']
  tags_out = ['      <value name="class">', '</value>\n']
  #'      <value name="class">0</value>'
  inserted_text = ""
  posA = 0
  for i in range(1924):
    posA = xml.find(tags_in[0], posA+len(inserted_text)+1)
    posA = xml.find(tags_in[1], posA)+len(tags_in[1])
    inserted_text = tags_out[0]+str(class_numbers[i])+tags_out[1]
    xml = xml[:posA] + inserted_text + xml[posA:]
  f = open("submission_" + task_no + ".xml", "w+")
  f.write(xml)
  f.close()
  print "done: " + task_no + " !"
