from nltk.stem.porter import *
stemmer = PorterStemmer()
sentence_0_raw = ['caresses', 'flies', 'dies', 'mules', 'denied',
            'died', 'agreed', 'owned', 'humbled', 'sized',
            'meeting', 'stating', 'siezing', 'itemization',
            'sensational', 'traditional', 'reference', 'colonizer',
            'plotted']
sentence_1_raw = ['caresses', 'flies', 'dies', 'mules', 'denied',
            'died', 'agreed', 'owned', 'humbled', 'sized',
            'meeting', 'stating', 'siezing', 'itemization',
            'sensational', 'traditional', 'reference', 'colonizer',
            'plotted']
sentence_0 = [stemmer.stem(plural) for plural in sentence_0_raw]
sentence_1 = [stemmer.stem(plural) for plural in sentence_1_raw]
indexes_0 = []
indexes_1 = []
n_x0 = len(sentence_0)
n_x1 = len(sentence_1)
for x0 in range(n_x0):
  for x1 in range(n_x1):
    if sentence_0[x0] == sentence_1[x1]:
      indexes_0.append(str(x0))
      indexes_1.append(str(x1))
print(' '.join(sentence_0))
print(' '.join(sentence_1))
print ' '.join(indexes_0)
print ' '.join(indexes_1)

