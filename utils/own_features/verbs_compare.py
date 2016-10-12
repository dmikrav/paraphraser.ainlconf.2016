import nltk

text = "I am very happy to be here today"
tokens = nltk.word_tokenize(text)
pos_tagged_tokens = nltk.pos_tag(tokens)
print pos_tagged_tokens
res = []
for x in pos_tagged_tokens:
  if 'v' == x[1].lower()[0:1]:
    res.append(x[0])
print res
