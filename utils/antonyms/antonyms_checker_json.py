import json
with open('../dataset.json') as data_file:    
  data = json.load(data_file)
  
data_copy = list(data)
N = len(data_copy)
print "NON-paraphrase", ([a["translations"]["yandex"]["antonym_bit"] for a in data_copy if a["class"] == "NON-paraphrase"])
print "Precise-paraphrase", len([a for a in data_copy if a["class"] == "Precise-paraphrase"])
print "Near-paraphrase", len([a for a in data_copy if a["class"] == "Near-paraphrase"])
