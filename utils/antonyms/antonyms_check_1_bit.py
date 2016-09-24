f = open("antonym_bit (copy).txt")
lines = f.readlines()
f.close()
#NON-paraphrase 2582
#Precise-paraphrase 1688
#Near-paraphrase 2957
ranges = [2582, 2582+1688, 1000000]
ranges_count = [0, 0, 0]
range_index = 0
for i in range(len(lines)):
  if i == ranges[range_index]:
    range_index += 1
  [x, y] = lines[i].split(" ")
  if int(y) == 1: 
    ranges_count[range_index] += 1 
print ranges_count
