import pygame, sys, copy, time, os
from CommandType import CommandType
from Turtle import Turtle
from helperFunctions import *
pygame.init()

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

def show(rules, axiom, customCommands={}, steps=10, stepsMulFactor=1, angle=90, n=5, res=(800,800), start_pos=(400,400), start_rot=0, widthOfLine=1, timeToDrawAllMs=0, delay=1000, printString=False, drawTurtle=True):
  # merging defaultCommands and defaultCommands
  commands = {k:v for (k,v) in defaultCommands.items()}
  for (key,val) in customCommands.items():
    commands[key] = val

  outputString = recursiveFindAndReplace(axiom,rules,n)
  print("String size: ",len(outputString))
  if printString:
    print(outputString)
  ##
  cmdsTodo = translateStringToCmds(commands,outputString)

  ## init drawingSurface for fractal
  drawingSurface = pygame.Surface((800,800))
  drawingSurface.fill((0,0,0,0)) # full transparent bg

  ## init pygame stuff
  clock = pygame.time.Clock()
  window = pygame.display.set_mode(res)
  font = pygame.font.SysFont(pygame.font.get_default_font(), 20)

  # init turtle state (position, rotation etc and stack)
  turtleState = Turtle(
    position=pygame.Vector2(start_pos),
    rotation=start_rot - 180,
    turningAngle = angle,
    stepLength = steps,
    color = (255,255,255),
    width = widthOfLine
  )
  stack = []

  # index of what command was last executed in each frame
  lastOperationIndexFloat = 0

  ### MAIN LOOP
  while True:
    ### EVENTS
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F1:
          if not os.path.exists("./screenshots"):
            os.makedirs("./screenshots")
          timeTaken = time.asctime(time.localtime(time.time())).replace(" ","_").replace(":","-")
          saveFile = "screenshots/"+timeTaken+".png"
          pygame.image.save(drawingSurface,saveFile)
          print("Screenshot saved as " + saveFile)

        if event.key == pygame.K_SPACE:
          # restart animation
          drawingSurface.fill((0,0,0,0))
          turtleState = Turtle(
            position=pygame.Vector2(start_pos),
            rotation=start_rot - 180,
            turningAngle = angle,
            stepLength = steps,
            color = (255,255,255),
            width = widthOfLine
          )
          stack = []
          lastOperationIndexFloat = len(cmdsTodo)
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
          lastOperationIndexFloat = 0


    ### CLEAR FRAME
    window.fill((0,0,0))

    ### TICKING
    dt = clock.tick()
    delay -= dt

    opsThisFrame = 0 # how many operations should be executed this frame
    if delay <= 0:
      # calculate how many operations should be executed this frame
      if timeToDrawAllMs == 0:
        opsThisFrame = len(cmdsTodo)
      else:
        opsThisFrame = float(len(cmdsTodo)) / timeToDrawAllMs * dt

      ## EXECUTE COMMANDS in this frame
      for (cmd, arg) in cmdsTodo[int(lastOperationIndexFloat):int(lastOperationIndexFloat + opsThisFrame)]:

        if cmd == CommandType.MOVE_FORWARD:
          if arg == None:
            arg = turtleState.stepLength
          newPosition = pygame.math.Vector2.rotate(pygame.Vector2(0,arg), turtleState.rotation) + turtleState.position
          turtleState.position = newPosition

        elif cmd == CommandType.DRAW_FORWARD:
          if arg == None:
            arg = turtleState.stepLength
          newPosition = pygame.math.Vector2.rotate(pygame.Vector2(0,arg), turtleState.rotation) + turtleState.position
          pygame.draw.line(drawingSurface, (255,255,255), turtleState.position, newPosition, turtleState.width)
          turtleState.position = newPosition

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
          print("Unknown command: " + str(cmd))

    if lastOperationIndexFloat < len(cmdsTodo):
      lastOperationIndexFloat += opsThisFrame
    else:
      lastOperationIndexFloat = len(cmdsTodo)

    # draw drawing surface on screen
    window.blit(drawingSurface, (0,0))

    # generate progress text on screen
    opsOutOfAll = font.render(str(int(lastOperationIndexFloat))+" / "+str(len(cmdsTodo)), True, (255,255,255))
    window.blit(opsOutOfAll, (0, 0))

    # draw turle on screen too?
    if drawTurtle:
      turtleState.draw(window)
    
    pygame.display.flip()
