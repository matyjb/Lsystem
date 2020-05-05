from enum import Enum
import pygame, sys

class CommandType:
  MOVE_FORWARD = 0
  DRAW_FORWARD = 1
  ROTATE_LEFT = 2
  ROTATE_RIGHT = 3
  PUSH = 4
  POP = 5

def filter_dict_by_prefix(d, filter_prefix):
    return {key:val for key, val in d.items() if key.startswith(filter_prefix)}

 
def getFinalString(substring,rules,n):
  if n==0:
    return substring
  
  s = substring
  for (key, val) in rules.items():
    s=s.replace(key,val)

  return getFinalString(s,rules,n-1)



def show(commands, axiom, rules, n=5, timePerStep=0, res=(800,800), start_pos=(400,400)):
  stack = []
  position = start_pos
  outputString = getFinalString(axiom,rules,n)
  print(outputString)
  ##
  window = pygame.display.set_mode(res)
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return


    # pobrać substring od i do j=i
    # przefiltrować ckomendy tym substringiem
    # jesli przefiltrowane komendy beda puste wywal errora
    # jesli nie beda sprawdz czy zawiera klucz == substringowi
    # # jesli tak to wykonaj komende, i=j+1 i wroc do pkt 2
    # # jesli nie to j++ i wroc do poczatku


    pygame.display.flip()
    

# Sierpinski triangle
# angle = 0
commands = {
  "F": (CommandType.DRAW_FORWARD,10),
  "G": (CommandType.DRAW_FORWARD,10),
  "+": (CommandType.ROTATE_LEFT,120),
  "-": (CommandType.ROTATE_RIGHT,120)
}
axiom = "F-G-G"
rules = {
  "F":"F-G+F+G-F", 
  "G":"GG"
}
n = 5
timePerStep = 1


# test = {"AABA":"a", "BAA":"b", "CCD":"c"}
# filt = filter_dict_by_prefix(test,"BA")
# print(filt)
show(commands,axiom,rules,n,timePerStep)