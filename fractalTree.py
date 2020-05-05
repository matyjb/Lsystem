from lsystem import *

steps = 3
angle = 45

commands = {
  "F": (CommandType.DRAW_FORWARD,steps),
  "G": (CommandType.DRAW_FORWARD,steps),
  "[": [(CommandType.PUSH,None), (CommandType.ROTATE_LEFT,angle)],
  "]": [(CommandType.POP,None), (CommandType.ROTATE_RIGHT,angle)]
}
axiom = "G"
rules = {
  "F":"FF", 
  "G":"F[G]G"
}
n = 8
show(commands,axiom,rules,n, start_pos=(400,800), msPerLine=5)