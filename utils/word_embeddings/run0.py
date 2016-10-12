import numpy as np
from numpy import linalg as la
import sys
# load the word embedding file
def load_embeddings(fname):
  f = (line.split(" ",1)[1] for line in file(fname))
  vecs = np.loadtxt(f)
  words = [line.split(" ",1)[0] for line in file(fname)]
  return words,vecs

words,vecs = load_embeddings("./wug_embeddings_d100/bow10.words")
norms = la.norm(vecs, axis=1)
nvecs = vecs / norms[:,np.newaxis]
vecs = nvecs
