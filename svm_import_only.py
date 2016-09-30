import sys
import os.path
from sklearn.svm import SVC
from sklearn import ensemble
from sklearn import cross_validation
import sklearn
from sklearn import metrics
import json
from pprint import pprint
import random
import numpy as np
import hashlib
from numpy import linalg as la
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
from nltk.corpus import genesis
import urllib2
from nltk.stem.wordnet import WordNetLemmatizer
import nltk
import re
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
brown_ic = wordnet_ic.ic('ic-brown.dat')
semcor_ic = wordnet_ic.ic('ic-semcor.dat')
genesis_ic = wn.ic(genesis, False, 0.0)

sys.path.append(os.path.abspath("./utils"))
from extract_ner_person_and_organization import get_ner_score as get_ner_score

