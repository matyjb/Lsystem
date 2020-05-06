from lsystem import *

steps = 5
angle = 90

commands = {
  "F": (CommandType.DRAW_FORWARD,steps),
  "-": (CommandType.ROTATE_LEFT,angle),
  "+": (CommandType.ROTATE_RIGHT,angle),
}
axiom = "FX"
rules = {
  "X":"X+YF+", 
  "Y":"-FX-Y"
}
n = 12
show(commands,axiom,rules,n, msPerLine=2)