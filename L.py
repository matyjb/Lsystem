# this file is used to run interpreter from terminal
from TurtleWindow import TurtleWindow
from Turtle import Turtle
import pygame, sys

#default values
axiom = ""
rules = {}
n = 0
angle = 0
stepLength = 10
startRot = 0
time = 0
delay = 0
printString=False
drawTurtle=True

args = list(reversed(sys.argv[1:]))
untranslatedRules = []
# first argument must be axiom
axiom = args.pop()

while len(args) > 0:
  arg = args.pop()
  if arg == "-R":
    while ":" in args[-1]:
      untranslatedRules.append(args.pop())
  
  elif arg == "-n":
    n = int(args.pop())
  
  elif arg == "-a":
    angle = float(args.pop())

  elif arg == "-s":
    stepLength = float(args.pop())

  elif arg == "-r":
    startRot = float(args.pop())

  elif arg == "-t":
    time = float(args.pop())
  
  elif arg == "-d":
    delay = float(args.pop())

  elif arg == "-S":
    printString = True

  elif arg == "-T":
    drawTurtle = True

# translate untranslatedRules into rules
for r in untranslatedRules:
  rr = r.split(':')
  rules[rr[0]] = rr[1]
###

turtleStartState = Turtle(
  position = pygame.Vector2(0,0),
  rotation = startRot,
  turningAngle = angle,
  stepLength = stepLength,
  mulStep = 1,
  mulAngle = 1,
  color = (255,255,255),
  width = 1
)

t = TurtleWindow(turtleStartState)
t.show(
  axiom = axiom,
  rules = rules,
  n = n,
  timeToDrawAllMs = time,
  delay = delay,
  drawTurtle = drawTurtle,
  printString = printString
)