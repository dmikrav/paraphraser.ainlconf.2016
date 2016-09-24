import urllib2
from nltk.stem.wordnet import WordNetLemmatizer
import nltk
import en
import re, json
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

def get_antonyms(word): 
 verbose = False
 try:
  response = urllib2.urlopen('http://www.thesaurus.com/browse/'+word.lower())
  html = response.read().lower()
  tags = [['            <section class="container-info antonyms" >', '            </section>']] 
  pos_tags = []
  inside = [['<span class="text">', '</span>']]
  for r in range(len(tags)):
    pos_start = 0
    tmp = []
    for c in range(len(tags[r])):
      tmp.append(html.find(tags[r][c], pos_start))
      if verbose: print pos_start, ":", tags[r][c]
    pos_tags.append(tmp)
  if verbose: print "\n", "=" * 80
  text = html[pos_tags[0][0]:pos_tags[0][1]]
  pos_end = 0
  res = []
  while True:
    pos_start = text.find(inside[0][0], pos_end)
    if pos_start == -1:
      break
    pos_start += len(inside[0][0])
    pos_end = text.find(inside[0][1], pos_start)
    res.append(text[pos_start:pos_end])
  if verbose: print res 
  if verbose: print "\n", "=" * 80
  if verbose: print html
 except:
  return [] 
 return res

def compute_opposite_flag(two_words):
  antonyms = [[], []]
  for i in range(2):
    antonyms[i] = get_antonyms(two_words[i].lower())
  if two_words[0] in antonyms[1] or two_words[1] in antonyms[0]:
    return 1
  return 0
   
def compute_opposite_list_flag(sentences):
  uncommon_words = get_uncommon_words(sentences)
  for w0 in uncommon_words[0]:
    for w1 in uncommon_words[1]:
      v0 = get_part_of_speech(' '.join(uncommon_words[0]), w0)
      if v0 not in ['v', 'n', 'a']: continue
      u0 = get_lemma(w0, v0)
      if v0.lower() == 'v':  
        u0 = en.verb.infinitive(u0)
      v1 = get_part_of_speech(' '.join(uncommon_words[1]), w1)
      if v1 not in ['v', 'n', 'a']: continue
      u1 = get_lemma(w1, v1)
      if v1.lower() == 'v':  
        u1 = en.verb.infinitive(u1)
      if compute_opposite_flag([u0, u1]) == 1:
        #print "@@:", u0, u1
        return 1
  return 0
  
 
def get_lemma(word, part_of_speech): 
  if part_of_speech not in ['v', 'n', 'a']: return word
  lemmatizer = WordNetLemmatizer()
  return lemmatizer.lemmatize(word, part_of_speech)
 

def get_part_of_speech_of_all_sentence(raw):
  for sentence in nltk.sent_tokenize(raw):
    sentence = nltk.pos_tag(nltk.wordpunct_tokenize(sentence))
    for word, pos in sentence:
      print word, pos

def are_first_halfs_of_word_equal(words):
  n = [0, 0]
  for i in range(2):
    n[i] = len(words[i])
  num = (min(n[0], n[1]) * 8) / 10
  if num < 3 : return False
  if 1.0 * max(n[0], n[1]) / min(n[0], n[1]) > 2 : return False
  return words[0][0:num] == words[1][0:num]

def get_part_of_speech(raw, word_to_search):
  word_to_search = word_to_search.lower()
  for sentence in nltk.sent_tokenize(raw):
    sentence = nltk.pos_tag(nltk.wordpunct_tokenize(sentence))
    for word, pos in sentence:
      if are_first_halfs_of_word_equal([word.lower(), word_to_search]):
        return pos[0:1].lower()

def get_uncommon_words(sentences):
  s = ["", ""]
  for i in range(2):
    s[i] = re.sub('[^a-zA-Z]+', ' ', sentences[i])
  lists = [s[0].split(" "), s[1].split(" ")]
  lists_stemmed = [[], []] 
  for i in range(2):
    for x in lists[i]:
      lists_stemmed[i].append(stemmer.stem(x).lower()) 
  common = list(set(lists_stemmed[0]).intersection(lists_stemmed[1]))
  #print common
  uncommon_indexes = [[], []]
  for i in range(len(lists_stemmed[0])):
    if lists_stemmed[0][i] not in common:
      uncommon_indexes[0].append(i)
  for i in range(len(lists_stemmed[1])):
    if lists_stemmed[1][i] not in common:
      uncommon_indexes[1].append(i)
  #print uncommon_indexes[0]
  #print uncommon_indexes[1]
  uncommon = [[], []]
  for i in range(2):
    for x in uncommon_indexes[i]:
      uncommon[i].append(lists[i][x])
  return uncommon



with open('../dataset.json') as data_file:    
  data = json.load(data_file)
  
data_copy = list(data)
lst = [[a["translations"]["yandex"]["pair"][0], a["translations"]["yandex"]["pair"][1]] for a in data_copy]

res = ""


for i in range(7227):
  print i
  f = open('antonym_bit.txt', 'a+')
  f.write(str(i)+" "+str(compute_opposite_list_flag(lst[i])) + "\n")
  f.close()


"""
s = [['U.S. Secretary of State John Kerry announced the deal with Russian Foreign Minister Sergei Lavrov late Friday in Geneva after a day of marathon negotiations.'],
     ['Rosstat: In 2012, food prices increased by 6.6 percent.',
      'Prices for food products in 2012 fell.']]
v0 = get_part_of_speech(s[1][0], w0)
'''
print get_part_of_speech(s[0][0], 'keRrY')
v = get_part_of_speech(s[0][0], 'announcment')
print v
u = get_lemma('announced', v)
print u
w0 = 'increased'
w1 = 'fell'
u0 = get_lemma(w0, v0)
print u0
v1 = get_part_of_speech(s[1][1], w1)
print v1
#u1 = get_lemma(w1, v1)
u1 = en.verb.infinitive(w1)
print u1
print compute_opposite_flag([u0, u1])
print get_uncommon_words(s[1])
'''
print compute_opposite_list_flag(s[1])
"""
'''
lst = [['rise', 'fall'], ['up', 'rise'], ['up', 'fall'], ['decrease', 'rise'], ['walk', 'rise'], ['buy', 'sell'], ['buy', 'rise'], ['do', 'rise']]

for i in range(len(lst)):
  print compute_opposite_flag(lst[i]), lst[i]
'''
