import re

def filter_dict_by_prefix(d, filter_prefix):
    return {key:val for key, val in d.items() if key.startswith(filter_prefix)}

# splituje txt podanymi separatoramia (jako krotka albo lista) i pozostawia separatory
# np. split("abfdcd",("a","c")) => ["a","bfd","c","d"]
def split(txt, separators):
  result = re.split("("+separators[0]+")",txt)
  for ss in separators[1:]:
    tmp = []
    for e in result:
      tmp += re.split("("+ss+")",e)
    result = tmp
  return result

def recursiveFindAndReplace(substring,rules,n):
  if n <= 0:
    return substring

  splitSubstring = split(substring,list(rules.keys()))
  #replace
  result = [rules[e] if e in rules.keys() else e for e in splitSubstring]
  return recursiveFindAndReplace(''.join(result),rules,n-1)

def translateStringToCmds(commands, string):
  result = []
  queue = string
  while len(queue):
    didTranslate = False
    for (key, value) in commands.items():
      if queue.startswith(key):
        if isinstance(value, list):
          for c in value:
            result.append(c)
        else:
          result.append(value)
        queue = queue[len(key):]
        didTranslate = True
        break
    if not didTranslate:
      queue = queue[1:]
    
  return result