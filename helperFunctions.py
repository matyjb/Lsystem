def filter_dict_by_prefix(d, filter_prefix):
    return {key:val for key, val in d.items() if key.startswith(filter_prefix)}


def recursiveFindAndReplace(substring,rules,n):
  if n <= 0:
    return substring

  outputString = []
  i=0
  while i < len(substring):
    didApplyRule = False
    for (key, val) in rules.items():
      if substring[i:].startswith(key):
        i += len(key)
        didApplyRule = True
        outputString.append(recursiveFindAndReplace(val,rules,n-1))
      
    if not didApplyRule:
      outputString.append(substring[i])
      i += 1

  return ''.join(outputString)

def getCmdsTodo(commands, string):
  # pobrać substring od i do j=i+1
  # przefiltrować ckomendy tym substringiem
  # jesli przefiltrowane komendy beda puste wywal errora
  # jesli nie beda sprawdz czy zawiera klucz == substringowi
  # # jesli tak to dodaj komende, i=j i wroc do pkt 2
  # # jesli nie to j++ i wroc do pkt 2
  i = 0
  j = 1
  result = []
  while i < len(string):
    possibleCmd = string[i:j]
    filteredCmds = filter_dict_by_prefix(commands,possibleCmd)
    if len(filteredCmds) == 0:
      # print("niezrozumiała komenda: " + possibleCmd)
      i = j
      j += 1
      continue
    
    if possibleCmd in filteredCmds.keys():
      # spr czy zostaly podane wiele komend jako jedna
      if isinstance(filteredCmds[possibleCmd], list):
        for c in filteredCmds[possibleCmd]:
          result.append(c)
      else:
        result.append(filteredCmds[possibleCmd])
      
      i = j
      j += 1
    else:
      j += 1

  return result