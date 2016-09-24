from nltk.corpus import wordnet as wn
lists = wn.synsets('good')
for x in range(len(lists)): 
  tmp = lists[x]
  print "synonym of good:  ", tmp, "  and it's antonyms are:"
  for i in range(len(tmp.lemmas())):
    tmp2 = tmp.lemmas()[i].antonyms()
    if tmp2 != []:
      print tmp2
  print '-' * 80
