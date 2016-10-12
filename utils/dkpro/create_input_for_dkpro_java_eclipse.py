# -*- coding: utf-8 -*-
# encoding=utf8  
import sys, json, re
reload(sys)  
sys.setdefaultencoding('utf8')

if __name__ == "__main__":
  lines = [[], [], []]
  for x in range(3):
    f = open("data_extracted_translations_test_set/extracted_google.txt")
    lines[x] = f.readlines()
    f.close()
  n = len(lines[0])/3
  res = ""
  for i in range(n):
    res += "==="
    for x in range(3):
      for y in range(2):
        res += lines[x][i*3+y] + "\n"
    res += "\n"
  f = open("all-1924.txt", "w+")
  f.write(res)
  f.close()
