from lsystem import *

steps = 10
angle = 60

commands = {
  "A": (CommandType.DRAW_FORWARD,steps),
  "B": (CommandType.DRAW_FORWARD,steps),
  "+": (CommandType.ROTATE_LEFT,angle),
  "-": (CommandType.ROTATE_RIGHT,angle)
}
axiom = "A"
rules = {
  "A":"B-A-B", 
  "B":"A+B+A"
}
n = 6
show(commands,axiom,rules,n, start_pos=(700,700), start_rot=-90)