from nltk.stem.porter import *
import re

regex = re.compile('[^a-zA-Z\ ]')
stemmer = PorterStemmer()
brands = ['google', 'yandex']
for a in range(len(brands)):
  file_name = 'translations_without_shared_words/all_' + brands[a]
  #print '\n', brands[a], '\n'
  f = open(file_name, 'r')
  content_lines = f.readlines()
  f.close()
  n = len(content_lines)/3
  tmp = ''
  for b in range(n):
    #print content_lines[b*3], content_lines[b*3+1]
    sentence_raw = [regex.sub('', content_lines[b*3].lower()).split(' '), regex.sub('', content_lines[b*3+1].lower()).split(' ')]
    sentence_stemmed = [[stemmer.stem(plural) for plural in sentence_raw[0]],
                        [stemmer.stem(plural) for plural in sentence_raw[1]]]
    list_input = [sentence_stemmed[0], sentence_stemmed[1]]
    list_indexes_that_stay = [[], []]
    list_result = [[],[]]
    common_elements = [item for item in list_input[0] if item in list_input[1]]
    for x in range(2):
      for i in range(len(list_input[x])):
        if not list_input[x][i] in common_elements:
          list_indexes_that_stay[x].append(i)
    for x in range(2):
      for i in range(len(list_indexes_that_stay[x])):
        list_result[x].append(sentence_raw[x][list_indexes_that_stay[x][i]])
    tmp += ' '.join(list_result[0]) + '\n'
    tmp += ' '.join(list_result[1]) + '\n'
    tmp += ' '.join(sentence_raw[0]) + '\n'
    tmp += ' '.join(sentence_raw[1]) + '\n' 
    tmp += '====================================' + '\n'
  file_name = 'translations_without_shared_words/only_different_words_' + brands[a]
  f = open(file_name, 'w+')
  f.write(tmp)
  f.close()
