import json
with open('test_json.json') as data_file:    
  data = json.load(data_file)
s = json.dumps(data, sort_keys=True, indent=4)
print s
s = s.replace("\\n", "\n")
with open('test_json_2.json', 'w') as outfile:
    json.dump(s, outfile)

