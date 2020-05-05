from lsystem import *

steps = 10
angle = 90

commands = {
  "F": (CommandType.DRAW_FORWARD,steps),
  "-": (CommandType.ROTATE_LEFT,angle),
  "+": (CommandType.ROTATE_RIGHT,angle),
  "X": (CommandType.DO_NOTHING,None),
  "Y": (CommandType.DO_NOTHING,None)
}
axiom = "FX"
rules = {
  "X":"X+YF+", 
  "Y":"-FX-Y"
}
n = 10
show(commands,axiom,rules,n, msPerLine=5)