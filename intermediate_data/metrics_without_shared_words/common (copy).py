from nltk.stem.porter import *
stemmer = PorterStemmer()
sentence_raw = [['caaresses', 'flies', 'dies', 'mules', 'denied',
            'died', 'agreed', 'ownded', 'humbled', 'sized',
            'meeting', 'stating', 'siezing', 'itemization',
            'sensational', 'traditional', 'reference', 'colonizer',
            'plotted'],
            ['a', 'caresses', 'flies', 'dies', 'mules', 'denied',
            'died', 'agreed', 'owned', 'humbled', 'sized',
            'meeting', 'stating', 'sriezing', 'itemization',
            'sensational', 'traditional', 'reference', 'colonizer',
            'plotted']]
sentence_stemmed = [[stemmer.stem(plural) for plural in sentence_raw[0]],
                    [stemmer.stem(plural) for plural in sentence_raw[1]]]

#list_input = [['a', 'e', 't', 'b', 'c'],
#              ['e', 'b', 'a', 'c', 'n', 's']]

list_input = [sentence_stemmed[0], sentence_stemmed[1]]
list_indexes_that_stay = [[], []]
list_result = [[],[]]
common_elements = [item for item in list_input[0] if item in list_input[1]]
print common_elements, '\n'
print '*@$' * 30
for x in range(2):
  for i in range(len(list_input[x])):
    if not list_input[x][i] in common_elements:
      list_indexes_that_stay[x].append(i)
print list_input[0]
print list_input[1]
print '~*#' * 30
print list_indexes_that_stay[0]
print list_indexes_that_stay[1]
print '-=-'*30
for x in range(2):
  for i in range(len(list_indexes_that_stay[x])):
    list_result[x].append(sentence_raw[x][list_indexes_that_stay[x][i]])
print list_result[0]
print list_result[1]
 
#for a in list_a
#print [list1.remove(a) for a in result]
#print [list2.remove(a) for a in result]
