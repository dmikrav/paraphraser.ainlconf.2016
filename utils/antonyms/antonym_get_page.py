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
        return 1, u0, u1
  return 0, '', ''
  
 
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



with open('../../dataset.json.bk') as data_file:    
  data = json.load(data_file)
  
data_copy = list(data)
lst = [[a["translations"]["yandex"]["pair"][0], a["translations"]["yandex"]["pair"][1]] for a in data_copy]

res = ""


listt = [u'0002589', u'0002590', u'0002658', u'0002669', u'0002699', u'0002729', u'0002730', u'0002737', u'0002740', u'0002805', u'0002852', u'0002899', u'0002947', u'0002966', u'0003003', u'0003061', u'0003083', u'0003097', u'0003247', u'0003275', u'0003283', u'0003311', u'0003397', u'0003484', u'0003854', u'0003877', u'0003887', u'0003903', u'0003911', u'0003939', u'0003946', u'0003954', u'0003957', u'0003986', u'0004029', u'0004037', u'0004043', u'0004121', u'0004123', u'0004166', u'0004176', u'0004179', u'0004192', u'0004231', u'0004232', u'0004347', u'0004381', u'0004434', u'0004451', u'0004460', u'0004490', u'0004516', u'0004517', u'0004591', u'0004637', u'0004647', u'0004661', u'0004671', u'0004704', u'0004707', u'0004730', u'0004739', u'0004758', u'0004775', u'0004796', u'0004817', u'0004821', u'0004869', u'0004911', u'0004951', u'0004957', u'0004976', u'0004977', u'0004978', u'0005028', u'0005032', u'0005185', u'0005200', u'0005282', u'0005284', u'0005348', u'0005413', u'0005456', u'0005457', u'0005485', u'0005526', u'0005602', u'0005655', u'0005716', u'0005718', u'0005759', u'0005785', u'0005823', u'0005834', u'0005853', u'0005897', u'0005954', u'0006029', u'0006036', u'0006046', u'0006153', u'0006234', u'0006313', u'0006401', u'0006427', u'0006578', u'0006660', u'0006739', u'0006801', u'0006813', u'0006909', u'0006959', u'0007125', u'0007167']
listt_res = []
for x in listt:
  listt_res.append(int(x)-1)

for i in range(7227):
  if i in listt_res:
    print i
    f = open('antonym_bit.txt', 'a+')
    f.write(str(i)+" "+str(compute_opposite_list_flag(lst[i])) + "\n" + lst[i][0] + "\n" + lst[i][1] + "\n\n")
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
