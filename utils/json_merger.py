import sys
import os.path
import json
import codecs

indexes_class = ['NON-paraphrase', 'Near-paraphrase', 'Precise-paraphrase']
semilar_analysis_file_name = ['analysis_output_class_-1', 'analysis_output_class_0', 'analysis_output_class_1']
google_translate_dir_name = 'full_en_google_semilar_output'
original_sentences_dir_name = 'original_sentences'
res = ''

js_1a = (
'''
{
  "source": [
'''
)
#the first sentence", "the second sentence"
js_1b = (
'''
  ],
  "class" : "''') 
js_2 = (
'''",
  "translations":{
    "google":{
      "pair": [
'''
)

js_3 = (
'''
      ],
      "features":{
'''
)

js_list = {'        "greedyComparerWNLin" : ', '        "optimumComparerLSATasa" : ', '        "dependencyComparerWnLeskTanim" : ', '        "cmComparer" : ', '        "bleuComparer" : ', '        "lsaComparer" : '}

js_4 = (
'''
      }
    }
  }
}
,
'''
)

def get_by_tag(tag, block):
  lines = block.split("\n")
  for i in lines:
    if i.find(tag) == 0:
      return i[len(tag):]
  return ""

list_of_tags = ["greedyComparerWNLin : ", "optimumComparerLSATasa : ", "dependencyComparerWnLeskTanim : ", "cmComparer : ", "bleuComparer : ", "lsaComparer : "]
list_of_tags_to_print = ["greedyComparerWNLin", "optimumComparerLSATasa", "dependencyComparerWnLeskTanim", "cmComparer", "bleuComparer", "lsaComparer"]
replace_list = ['\\xe7', '\\xe9', '\\xa3', '\\xf4', '\\xe1', '\\u012d', '\\u20ac', '\\xe3', '\\u015f', '\\u0103', '\\xf4', '\\xf4']

res = '['
cnt = 0
for i in range(3):
  full_file_name = os.path.join(google_translate_dir_name, semilar_analysis_file_name[i])
  f = open(full_file_name, "r")
  s = f.read()
  f.close()
  blocks = s.split("                              \n")

  full_file_name = os.path.join(original_sentences_dir_name, str(i-1))
  f = open(full_file_name, "r")
  s = f.read()
  f.close()
  original_sentences = s.split("====================================\n")
  if len(blocks) != len(original_sentences):
    raise Exception("NOT equal length: " + str(len(blocks)) + " " + str(len(original_sentences)))  

  n = len(blocks)

  for x in range(n):
    tab1 = "    "
    tab2 = "        "
    sent = original_sentences[x].split("\n")
    if len(sent) < 2:
      continue
    res += js_1a
    res += tab1 + '"' + sent[0].replace('"', ' ') + '", \n' + tab1 + '"' + sent[1].replace('"', ' ') + '"'
    res += js_1b
    res += indexes_class[i]
    res += js_2
    google_eng_sent_1 = get_by_tag("Sentence 1:", blocks[x])
    google_eng_sent_2 = get_by_tag("Sentence 2:", blocks[x])
    for uuu in replace_list:
      google_eng_sent_1 = google_eng_sent_1.replace(uuu, '')
      google_eng_sent_2 = google_eng_sent_2.replace(uuu, '')
    res += tab2 + '"' + google_eng_sent_1 + '",\n'
    res += tab2 + '"' + google_eng_sent_2 + '"'
    res += js_3
    if len(blocks) < 5:
      continue
    for y in range(len(list_of_tags)):
      a = get_by_tag(list_of_tags[y], blocks[x])
      if a == "NaN":
        a = "0"
      res += tab2 + '"' + list_of_tags_to_print[y] + '" : ' + a + ',\n'
    res = res[:-2]
    res += js_4
res = res[:-2]
res += "]"

full_file_name = "merged.json"
f = codecs.open(full_file_name, "w+", "utf-8")
f.write(res)
f.close()
print "   output in file  merged.json  -  Done\n"
print "   file  merged.json  -  Test"
with open('merged.json') as data_file:    
  data = json.load(data_file)
print data[0]["source"][0]
print len(data[0])	
print "   file  merged.json  -  Test passed"
sys.exit()

