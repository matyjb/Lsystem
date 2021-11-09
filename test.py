import re
import numpy as np

def split(txt, s):
  result = re.split("("+s[0]+")",txt)
  for ss in s[1:]:
    tmp = []
    for e in result:
      tmp += re.split("("+ss+")",e)
    result = tmp
  return result


s = ("aa","bb","cc")
txt = "fccdsvaaaccfdsfccbbfccdsvcaavbbb"
# txt = re.split("("+s[0]+")",txt)
# print(txt)
# txt2 = []
# for e in txt:
#   txt2 += re.split("("+s[1]+")",e)
print(txt)
print(split(txt,s))
print(''.join(split(txt,s)))
