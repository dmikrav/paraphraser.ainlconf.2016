import sys
import os.path
import json


google_translate_dir_name = "full_en_semilar_output"
google_translate_file_names = ["-1", "0", "1"]
original_sentences_dir_name = "original_sentences"
google_translate_file_names = [""]
res = ""

te_1 = (
'''
{
  "source": 
    ["The first sentence", "The second sentence"],
  "class":"none",
  "Original": [
'''
)

te_2a = (
'''
  "translations":{
    "Google":{
      "pair": [
'''
)

te_2b = '        '

te_3 = (
'''
],
      "features":{
'''
)

te_4 = '        "greedyComparerWNLin" : '
te_5 = '        "optimumComparerLSATasa" : '
te_6 = '        "dependencyComparerWnLeskTanim" : '
te_7 = '        "cmComparer" : '
te_8 = '        "bleuComparer" : '
te_9 = '        "lsaComparer" : '

te_10 = (
'''
        }
      }
    }
  }
,
'''
)





#with open('example.json') as data_file:    
#  data = json.load(data_file)
#print(data)


#print data[0]["source"][0]
#print len(data[0])	
#sys.exit()

