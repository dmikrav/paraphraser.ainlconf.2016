import json
with open('../dataset.json') as data_file:    
  data = json.load(data_file)
  
data_copy = list(data)
N = len(data_copy)
print "N:", N

for task_no in range(1):

  classes_ids = [[], []]

  print "NON-paraphrase", len([a for a in data_copy if a["class"] == "NON-paraphrase"])

  print "Precise-paraphrase", len([a for a in data_copy if a["class"] == "Precise-paraphrase"])

  print "Near-paraphrase", len([a for a in data_copy if a["class"] == "Near-paraphrase"])
