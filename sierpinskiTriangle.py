from TurtleWindow import TurtleWindow
from CommandType import CommandType

t = TurtleWindow()
t.turtle.stepLength=10
t.turtle.turningAngle=120

commands = {
  "G": (CommandType.DRAW_FORWARD,None),
}
axiom = "F+G+G"
rules = {
  "F":"F+G-F-G+F", 
  "G":"GG"
}
t.show(
  axiom,
  rules,
  customCommands=commands,
  n=5,
  timeToDrawAllMs=1000
  )