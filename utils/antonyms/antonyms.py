from nltk.corpus import wordnet as wn

def is_there_part_of_speech(part_of_speech, synsets):
  n = len(synsets)
  for i in range(n):
    s = str(synsets[i])
    if s.find('.'+part_of_speech+'.') != -1:
      return True
  return False
#---------------------------------------------------------
def get_first_synset_part_of_speech(part_of_speech, synsets):
  n = len(synsets)
  for i in range(n):
    s = str(synsets[i])
    if s.find('.'+part_of_speech+'.') != -1:
      return synsets[i]
  return None


lst_antonyms = [['Add', 'Subtract'], ['Above', 'Below'], ['After', 'Before'], ['Awake', 'Asleep'], ['Bad', 'Good'],['Better', 'Worse'], ['Big', 'Little'], ['Birth', 'Death'], ['Boy', 'Girl'],['Clean', 'Dirty'],['Close', 'Open'],['Cold', 'Hot'],['End', 'Begin'],['Dark', 'Light'],['Day', 'Night'],['Even', 'Odd'],['Fail', 'Pass'],['False', 'True'],['East', 'West'],['Fat', 'Skinny'],['Hungry', 'Full'],['Gentle', 'Rough'],['Float', 'Sink'],['Happy', 'Sad'],['Hard', 'Soft'],['Heavy', 'Light'],['High', 'Low'],['In', 'Out'],['Last', 'First'],['Laugh', 'Cry'],['Learn', 'Teach'],['Less', 'More'],['Lie', 'Truth'],['Long', 'Short'],['Loose', 'Tight'],['Lost', 'Found'],['Love', 'Hate'],['North', 'South'],['On', 'Off'],['Over', 'Under'],['Play', 'Work'],['Polite', 'Rude'],['Poor', 'Rich'],['Present', 'Absent'],['Top', 'Bottom'],['Quick', 'Slow'],['Raise', 'Lower'],['Right', 'Wrong'],['Rise', 'Sink'],['Rough', 'Smooth'],['Same', 'Different'],['Sell', 'Buy'],['Short', 'Long'],['Sour', 'Sweet'],['Start', 'Stop'],['Stay', 'Leave'],['Stop', 'Go'],['Strong', 'Weak'],['Teacher', 'Student'],['Tidy', 'Messy'],['True', 'False'],['Ugly', 'Beautiful'],['Up', 'Down'],['White', 'Black'],['Wild', 'Tame'],['Win', 'Lose'],['Well', 'Sick'],['Wet', 'Dry'],['Young', 'Old']]

lst_synonyms = [['Afraid', 'scared'],
['Auto', 'car'],
['Big', 'large', 'huge'],
['Blank', 'empty', 'hollow'],
['Bunny', 'rabbit', 'hare'],
['Cap', 'hat'],
['Center', 'middle', 'inside'],
['Couch', 'sofa', 'divan'],
['Evil', 'bad', 'wicked'],
['Famous', 'well-known'],
['Father', 'dad', 'daddy'],
['Funny', 'silly', 'playful', 'crazy'],
['Garbage', 'trash', 'junk', 'waste'],
['Gloomy', 'sad', 'unhappy'],
['Happy', 'glad', 'joyful', 'cheerful'],
['Hide', 'cover'],
['House', 'home'],
['Ill', 'sick'],
['Idea', 'thought'],
['Jog', 'run'],
['Listen', 'hear'],
['Little', 'small', 'tiny'],
['Look', 'see', 'glance', 'stare'],
['Mad', 'angry', 'furious'],
['Mother', 'mom', 'mommy'],
['Neat', 'tidy', 'clean'],
['Present', 'gift', 'reward', 'award'],
['Quick', 'fast', 'swift'],
['Quiet', 'calm'],
['Rest', 'relax'],
['Rock', 'stone'],
['Rug', 'carpet', 'mat'],
['Sack', 'bag', 'backpack'],
['Sniff', 'smell', 'inhale'],
['Strange', 'odd', 'weird'],
['Tall', 'high', 'big'],
['True', 'right', 'correct'],
['Under', 'below', 'beneath'],
['Woman', 'lady', 'female'],
['Yell', 'shout', 'scream']]

synset = [None, None]
labels = ['Antonyms', 'Synonyms']
for y in range(2):
 print '=' * 80, '\n', labels[y], '\n'
 if y == 0: lstA = lst_antonyms
 if y == 1: lstA = lst_synonyms
 n = len(lstA) 
 totals = [0, 0, 0]
 totals_n = 0
 for i in range(n):
  s = [lstA[i][0], lstA[i][1]]
  part_os_lst = ['v', 'n']
  for x in range(len(part_os_lst)):
    p = part_os_lst[x]
    synset_lst = [wn.synsets(s[0]), wn.synsets(s[1])]
    #print synset_lst[0]
    #print ''
    #print synset_lst[1]
    #print ''
    is_pos = [is_there_part_of_speech(p, synset_lst[0]), is_there_part_of_speech(p, synset_lst[1])]
    if is_pos[0] and is_pos[1]:
      synset = [get_first_synset_part_of_speech(p, synset_lst[0]), get_first_synset_part_of_speech(p, synset_lst[1])]
      #print synset[0]
      #print '-' * 5
      #print synset[1]
      #print '-' * 5
      break
  '''
  if synset[0] == None or synset[1] == None:
    if synset[0] == None: print "    none: ", s[0]  
    if synset[1] == None: print "    none: ", s[1]  
    print "-" * 80
    continue
  '''
  tmp = [synset[0].path_similarity(synset[1]), synset[0].lch_similarity(synset[1]), synset[0].wup_similarity(synset[1])]
  totals_n += 1
  for v in range(3):
    totals[v] += tmp[v]
  res = str(tmp[0])
  res += "; " + str(tmp[1])
  res += "; " + str(tmp[2])
  print s[0], s[1], ':', res
 print "\n", "     Total averages:  ", totals[0]/totals_n, totals[1]/totals_n, totals[2]/totals_n, "\n"
