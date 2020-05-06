from lsystem import *

commands = {
  "G": (CommandType.DRAW_FORWARD,None),
}
axiom = "F"
rules = {
  "F":"G+F+G", 
  "G":"F-G-F"
}
show(
  rules,
  axiom,
  customCommands=commands,
  steps=10,
  angle=60,
  n=6,
  start_pos=(700,700),
  start_rot=-90,
  opPerSec=2000
  )