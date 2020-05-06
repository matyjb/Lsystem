from lsystem import *

commands = {
  "G": (CommandType.DRAW_FORWARD,None),
  "[": [(CommandType.PUSH,None), (CommandType.ROTATE_LEFT,None)],
  "]": [(CommandType.POP,None), (CommandType.ROTATE_RIGHT,None)]
}
axiom = "G"
rules = {
  "F":"FF", 
  "G":"F[G]G"
}
show(
  rules,
  axiom,
  steps=3,
  angle=45,
  customCommands=commands,
  n=8,
  start_pos=(400,800),
  msPerLine=5
  )