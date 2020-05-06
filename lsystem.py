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
  if n <= 0:
    return substring

  outputString = ""
  i=0
  while i < len(substring):
    didApplyRule = False
    for (key, val) in rules.items():
      if substring[i:].startswith(key):
        i += len(key)
        didApplyRule = True
        outputString += getFinalString(val,rules,n-1)
      
    if not didApplyRule:
      outputString += substring[i]
      i += 1

  return outputString


def getCmdsTodo(commands, string):
  # pobrać substring od i do j=i+1
  # przefiltrować ckomendy tym substringiem
  # jesli przefiltrowane komendy beda puste wywal errora
  # jesli nie beda sprawdz czy zawiera klucz == substringowi
  # # jesli tak to dodaj komende, i=j i wroc do pkt 2
  # # jesli nie to j++ i wroc do pkt 2
  i = 0
  j = 1
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
          yield c
      else:
        yield filteredCmds[possibleCmd]
      
      i = j
      j += 1
    else:
      j += 1

  # return result  

def show(commands, axiom, rules, n=5, res=(800,800), start_pos=(400,400), start_rot=0, widthOfLine=1, msPerLine=0, delay=1000):
  outputString = getFinalString(axiom,rules,n)
  ##
  clock = pygame.time.Clock()
  window = pygame.display.set_mode(res)

  timeFromStartMs = 0
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

    window.fill((0,0,0))
    timeFromStartMs += clock.tick()
    # print(timeFromStartMs)

    # init state (position, rotation, stack)
    position = pygame.Vector2(start_pos)
    rotation = start_rot - 180
    stack = []
    if delay <= timeFromStartMs:
      linesDrawn = 0
      for (cmd, arg) in getCmdsTodo(commands,outputString):
        if linesDrawn * msPerLine >= timeFromStartMs-delay:
          break

        if cmd == CommandType.MOVE_FORWARD:
          newPosition = pygame.math.Vector2.rotate(pygame.Vector2(0,arg), rotation) + position
          position = newPosition
        elif cmd == CommandType.DRAW_FORWARD:
          newPosition = pygame.math.Vector2.rotate(pygame.Vector2(0,arg), rotation) + position
          pygame.draw.line(window, (255,255,255), position, newPosition, widthOfLine)
          position = newPosition
          linesDrawn += 1
        elif cmd == CommandType.ROTATE_LEFT:
          rotation += arg
          if rotation > 180:
            rotation -= 360
        elif cmd == CommandType.ROTATE_RIGHT:
          rotation -= arg
          if rotation < -180:
            rotation += 360
        elif cmd == CommandType.PUSH:
          stack.append((position,rotation))
        elif cmd == CommandType.POP:
          (newPos,newRot) = stack.pop()
          position = newPos
          rotation = newRot
        else:
          print("Nieznana komenda - " + str(cmd))



    pygame.display.flip()
