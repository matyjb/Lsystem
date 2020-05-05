from lsystem import *

steps = 10
angle = 90

commands = {
  "F": (CommandType.DRAW_FORWARD,steps),
  "-": (CommandType.ROTATE_LEFT,angle),
  "+": (CommandType.ROTATE_RIGHT,angle),
}
axiom = "F"
rules = {
  "F":"F-F+F+F-F"
}
n = 3
show(commands,axiom,rules,n, msPerLine=10)