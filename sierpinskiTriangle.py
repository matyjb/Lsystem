from lsystem import *

commands = {
  "G": (CommandType.DRAW_FORWARD,None),
}
axiom = "F+G+G"
rules = {
  "F":"F+G-F-G+F", 
  "G":"GG"
}
show(
  rules,
  axiom,
  customCommands=commands,
  steps=10,
  angle=120,
  n=5,
  opPerSec=2000
  )