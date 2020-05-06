from lsystem import *

commands = {
  "G": (CommandType.DRAW_FORWARD,None),
}
axiom = "F"
rules = {
  "F":"F+G++G-F--FF-G+",
  "G":"-F+GG++G+F--F-G"
}
show(
  rules,
  axiom,
  customCommands=commands,
  steps=10,
  angle=60,
  n=4,
  start_pos=(700,300),
  opPerSec=2000
  )