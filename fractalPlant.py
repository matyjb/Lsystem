from lsystem import *

steps = 2
angle = 25

commands = {
  "F": (CommandType.DRAW_FORWARD,steps),
  "-": (CommandType.ROTATE_LEFT,angle),
  "+": (CommandType.ROTATE_RIGHT,angle),
  "X": (CommandType.DO_NOTHING,None),
  "[": (CommandType.PUSH,None),
  "]": (CommandType.POP,None)
}
axiom = "X"
rules = {
  "X":"F+[[X]-X]-F[-FX]+X", 
  "F":"FF"
}
n = 7
show(commands,axiom,rules,n, start_pos=(10,800), start_rot=30)