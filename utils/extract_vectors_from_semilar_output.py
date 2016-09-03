import os.path

def get_by_tag(tag, block):
  lines = block.split("\n")
  for i in lines:
    if i.find(tag) == 0:
      return i[len(tag):]
  return ""

dir_name = "RESULTS_ON_FIRST_40_KB_OF_INPUT_FILES_FOR_EACH_OF_3_CLASSES"
file_list = ["analysis_output_class_NEAR_PARAPHRAZES", "analysis_output_class_NON_PARAPHRAZES", "analysis_output_class_PRECISE_PARAPHRAZES"]
file_output_list = ["NEAR_PARAPHRAZES", "NON_PARAPHRAZES", "PRECISE_PARAPHRAZES"]
indexes = ["0", "-1", "1"]
list_of_tags = ["greedyComparerWNLin : ", "optimumComparerLSATasa : ", "dependencyComparerWnLeskTanim : ", "cmComparer : ", "bleuComparer : ", "lsaComparer : "]

for i in range(3):
  full_file_name = os.path.join(dir_name, file_list[i])
  f = open(full_file_name, "r")
  s = f.read()
  f.close()
  blocks = s.split("                              ")
  res = ""
  for block in blocks:
    tmp = ""
    if len(block) < 5:
      continue
    for tag in list_of_tags:
      a = get_by_tag(tag, block)
      if a == "NaN":
        a = "0"
      tmp += a + ","
    tmp = tmp[:-1]
    res += tmp	 + "\n"
  full_file_name = os.path.join(dir_name, indexes[i])
  f = open(full_file_name, "w+")
  f.write(res)
  f.close()
  

#Sentence 1:Police allowed to shoot to kill citizens with travmatiki.
#Sentence 2:Police may allow hooligans to shoot at travmatiki.
#------------------------------
#greedyComparerWNLin : 0.59954286
#optimumComparerLSATasa : 0.72727275
#dependencyComparerWnLeskTanim : 0.49822506
#cmComparer : 0.84466743
#bleuComparer : 0.0
#lsaComparer : 0.5599317
