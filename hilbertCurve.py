from lsystem import *

steps = 10
angle = 90

commands = {
  "-": (CommandType.ROTATE_LEFT,angle),
  "+": (CommandType.ROTATE_RIGHT,angle),
  "F": (CommandType.DRAW_FORWARD, steps)
}
axiom = "A"
rules = {
  "A":"-BF+AFA+FB-", 
  "B":"+AF-BFB-FA+"
}
n = 6
show(commands,axiom,rules,n, start_pos=(0,799), msPerLine=2)