import sys
import json
import hashlib
import os, os.path
import inspect, os

localdir =  os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) # script directory

def get_json(string):
    strmd5 = hashlib.md5(string).hexdigest()

    if (not os.path.exists(localdir+"/../json/"+strmd5+".json")):
        #raise ValueError("file not found: '"+string+"'")
        return None

    with open(localdir+"/../json/"+strmd5+".json") as data_file:
        return json.load(data_file)

