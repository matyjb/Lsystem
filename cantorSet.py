from lsystem import *

steps = 2

commands = {
  "F": (CommandType.DRAW_FORWARD,steps),
  "G": (CommandType.MOVE_FORWARD,steps),
}
axiom = "F"
rules = {
  "F":"FGF", 
  "G":"GGG"
}
n = 6
show(commands,axiom,rules,n, start_pos=(0,400), start_rot=90, widthOfLine=3)