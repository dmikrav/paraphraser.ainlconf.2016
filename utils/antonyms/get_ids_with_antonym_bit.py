import json
classes_names = ["NON-paraphrase", "Near-paraphrase", "Precise-paraphrase"]
with open('../../dataset.json.bk') as data_file:    
  data = json.load(data_file)
data_copy = list(data)
listt = [[[a['translations']['yandex']['antonym_bit'], a['class'], a['id'], a['translations']['yandex']['pair']]] for a in data_copy if a['translations']['yandex']['antonym_bit']]
listt_2 = [a['id'] for a in data_copy if a['translations']['yandex']['antonym_bit'] == 1 and a['class'] != classes_names[0]]
print len(listt_2)
print listt_2

