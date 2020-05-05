from lsystem import *

steps = 10
angle = 120

commands = {
  "F": (CommandType.DRAW_FORWARD,steps),
  "G": (CommandType.DRAW_FORWARD,steps),
  "-": (CommandType.ROTATE_LEFT,angle),
  "+": (CommandType.ROTATE_RIGHT,angle)
}
axiom = "F+G+G"
rules = {
  "F":"F+G-F-G+F", 
  "G":"GG"
}
n = 5
show(commands,axiom,rules,n, msPerLine=5)