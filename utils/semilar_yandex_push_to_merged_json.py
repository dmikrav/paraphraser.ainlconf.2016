f = open("yandex_translate/analysis_yandex_")
lines_semilar = f.readlines()
f.close()
f = open("merged_yandex.json")
content_json = f.read()
f.close()
tagA = '            "yandex": {'
tagB = '                "pair": ['
tagC = '                ]'

tag = [',',
 '                "features": {',
 '                    "greedyComparerWNLin": ',
 '                    "optimumComparerLSATasa": ',
 '                    "dependencyComparerWnLeskTanim": ',
 '                    "cmComparer": ',
 '                    "bleuComparer": ',
 '                    "lsaComparer": ',
 '                }']

pos = 0
for i in range(7227):
  pos = content_json.find(tagA, pos)
  pos = content_json.find(tagB, pos)
  pos = content_json.find(tagC, pos)
  pos += len(tagC)
  tmp = ''
  for x in range(9):
    if x == 0 or x == 1 or x == 8:
      sofit = '\n'
      if x == 8:
        sofit = ''
      tmp += tag[x] + sofit
    else:
      pattern = ' : '
      posb = lines_semilar[i*10+3+(x-2)].find(pattern) + len(pattern)
      number = lines_semilar[i*10+3+(x-2)][posb:-1]
      if number.find('NaN') != -1:
        number = '0'
      tmp += tag[x] + number + ',\n'
      if x == 7:
        tmp = tmp[:-2] + '\n'
  content_json = content_json[0:pos] + tmp + content_json[pos:]

f = open("with_semilar_of_yandex.json", "w+")
f.write(content_json)
f.close()

