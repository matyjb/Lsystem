from enum import Enum
import pygame, sys, copy, time, os

class TurtleState:
  def __init__(self,position,rotation,turningAngle,stepLength,color,width):
    self.position = position
    self.rotation = rotation
    self.turningAngle = turningAngle
    self.stepLength = stepLength
    self.color = color
    self.width = width


class CommandType:
  MOVE_FORWARD = 0
  DRAW_FORWARD = 1
  ROTATE_LEFT = 2
  ROTATE_RIGHT = 3
  PUSH = 4
  POP = 5
  INC_LINE_WIDTH = 6
  DEC_LINE_WIDTH = 7
  DRAW_DOT = 8
  INC_ANGLE = 9
  DEC_ANGLE = 10
  MUL_STEPS = 11
  DIV_STEPS = 12


def filter_dict_by_prefix(d, filter_prefix):
    return {key:val for key, val in d.items() if key.startswith(filter_prefix)}

 
def getFinalString(substring,rules,n):
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
        outputString.append(getFinalString(val,rules,n-1))
      
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

defaultCommands = {
  "F": (CommandType.DRAW_FORWARD,None),
  "f": (CommandType.MOVE_FORWARD,None),
  "[": (CommandType.PUSH,None),
  "]": (CommandType.POP,None),
  "-": (CommandType.ROTATE_LEFT,None),
  "+": (CommandType.ROTATE_RIGHT,None),
  "|": (CommandType.ROTATE_LEFT,180),
  "#": (CommandType.INC_LINE_WIDTH,None),
  "!": (CommandType.DEC_LINE_WIDTH,None),
  "@": (CommandType.DRAW_DOT,None),
  ")": (CommandType.INC_ANGLE,None),
  "(": (CommandType.DEC_ANGLE,None),
  ">": (CommandType.MUL_STEPS,None),
  "<": (CommandType.DIV_STEPS,None),
}

def show(rules, axiom, customCommands={}, steps=10, stepsMulFactor=1, angle=90, n=5, res=(800,800), start_pos=(400,400), start_rot=0, widthOfLine=1, opPerSec=0, delay=1000, printString=False):
  # merging defaultCommands and defaultCommands
  commands = {k:v for (k,v) in defaultCommands.items()}
  for (key,val) in customCommands.items():
    commands[key] = val

  outputString = getFinalString(axiom,rules,n)
  print("String size: ",len(outputString))
  if printString:
    print(outputString)
  ##
  cmdsTodo = [i for i in getCmdsTodo(commands,outputString)]
  clock = pygame.time.Clock()
  window = pygame.display.set_mode(res)
  # init state (position, rotation, stack)
  turtleState = TurtleState(
    position=start_pos,
    rotation=start_rot - 180,
    turningAngle = angle,
    stepLength = steps,
    color = (255,255,255),
    width = widthOfLine
  )
  stack = []

  timeFromStartMs = 0
  lastOperation = 0
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F1:
          if not os.path.exists("./screenshots"):
            os.makedirs("./screenshots")
          timeTaken = time.asctime(time.localtime(time.time())).replace(" ","_").replace(":","-")
          saveFile = "screenshots/"+timeTaken+".png"
          pygame.image.save(window,saveFile)
          print("Screenshot saved as " + saveFile)



    # window.fill((0,0,0))
    dt = clock.tick()
    timeFromStartMs += dt


    # print(timeFromStartMs)
    opsThisFrame = 0
    if delay <= timeFromStartMs:
      if opPerSec == 0:
        opsThisFrame = len(cmdsTodo)
      else:
        opsThisFrame = int(opPerSec * dt / 1000.0)
      # linesDrawn = 0 # used for animation
      for (cmd, arg) in cmdsTodo[lastOperation:lastOperation + opsThisFrame]:
        # if linesDrawn * msPerLine >= timeFromStartMs-delay:
        #   break

        if cmd == CommandType.MOVE_FORWARD:
          if arg == None:
            arg = turtleState.stepLength
          newPosition = pygame.math.Vector2.rotate(pygame.Vector2(0,arg), turtleState.rotation) + turtleState.position
          turtleState.position = newPosition

        elif cmd == CommandType.DRAW_FORWARD:
          if arg == None:
            arg = turtleState.stepLength
          newPosition = pygame.math.Vector2.rotate(pygame.Vector2(0,arg), turtleState.rotation) + turtleState.position
          pygame.draw.line(window, (255,255,255), turtleState.position, newPosition, turtleState.width)
          turtleState.position = newPosition
          # linesDrawn += 1

        elif cmd == CommandType.ROTATE_LEFT:
          if arg == None:
            arg = turtleState.turningAngle
          turtleState.rotation += arg
          if turtleState.rotation > 180:
            turtleState.rotation -= 360

        elif cmd == CommandType.ROTATE_RIGHT:
          if arg == None:
            arg = turtleState.turningAngle
          turtleState.rotation -= arg
          if turtleState.rotation < -180:
            turtleState.rotation += 360

        elif cmd == CommandType.PUSH:
          if arg == None:
            stack.append(copy.copy(turtleState))
          else:
            stack.append(arg)

        elif cmd == CommandType.POP:
          turtleState = stack.pop()

        elif cmd == CommandType.INC_LINE_WIDTH:
          if arg == None:
            turtleState.width += 1
          else:
            turtleState.width += arg

        elif cmd == CommandType.DEC_LINE_WIDTH:
          if arg == None:
            turtleState.width -= 1
          else:
            turtleState.width -= arg
            
          if turtleState.width <= 0:
            turtleState.width = 1

        elif cmd == CommandType.DRAW_DOT:
          if arg == None:
            pygame.draw.circle(screen, (255,255,255), turtleState.position, turtleState.width)
          else:
            pygame.draw.circle(screen, (255,255,255), turtleState.position, arg)

        elif cmd == CommandType.INC_ANGLE:
          if arg == None:
            turtleState.turningAngle += 1
          else:
            turtleState.turningAngle += arg

        elif cmd == CommandType.DEC_ANGLE:
          if arg == None:
            turtleState.turningAngle -= 1
          else:
            turtleState.turningAngle -= arg

          if turtleState.turningAngle <= 0:
            turtleState.turningAngle = 1

        elif cmd == CommandType.MUL_STEPS:
          if arg == None:
            turtleState.stepLength *= stepsMulFactor
          else:
            turtleState.stepLength *= arg

        elif cmd == CommandType.DIV_STEPS:
          if arg == None:
            turtleState.stepLength /= float(stepsMulFactor)
          else:
            turtleState.stepLength /= float(arg)

        else:
          print("Nieznana komenda - " + str(cmd))


    lastOperation += opsThisFrame
    windowCopy = window.copy()
    window.blit(windowCopy, (0,0))
    pygame.display.flip()
