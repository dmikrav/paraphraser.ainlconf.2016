import difflib

sm = difflib.SequenceMatcher(None)
listt = [["Returning from Syria Russians are concerned about employment in their homeland.",
"Emergencies Ministry aircraft will take out the Russians from Syria destroyed. "],
["Returning from Syria, the Russians are concerned about the issue of employment at home.",
"Emergency situations Ministry planes will take out the Russians from the destroyed"],
["In Istanbul, the police, with the support of armored vehicles dispersed the demonstrators.",
"The police dispersed the demonstrators in Taksim Square in Istanbul. "],
["In Istanbul, police supported by armored vehicles dispersed the demonstrators.",
"Police dispersed demonstrators on Taksim square in Istanbul."],
["Ex-cop krysheval Matveevskoe merchant market, was arrested.",
"Police arrested a Matveevskoe market. "],
["Ex-COP fronting dealer MATVEEVSKOE market, arrested.",
"Police Matveyevskoye market was arrested."],
["The Supreme Court requires materials cases of Mikhail Khodorkovsky and Platon Lebedev.", 
"The Supreme Court requested the case against Khodorkovsky and Lebedev. "],
["The Supreme court requires the records of M. Khodorkovsky and P. Lebedev.",
"The Supreme court asked the case of Khodorkovsky and Lebedev."],
["She died first guitarist of Yes,  architect prog rock  Peter Banks.", 
"Died Yes guitarist Peter Banks. "],
["Died the first guitarist for Yes, the architect of prog rock Peter banks.",
"Died guitarist of Yes Peter banks."]]
switch_to = [0, 2, 6, 10000]
a = ["non", "near", "precise"]
i = 0
curr = 0
for [x, y] in listt:
  if i == switch_to[curr]:
    print  "\n", "=" * 70, "\n", a[curr], "\n", "-" * 70, "\n"
    curr += 1
  i += 1
  sm.set_seq2(x)
  sm.set_seq1(y)
  print "\n", x, "\n", y, "\n", sm.ratio(), "\n"

