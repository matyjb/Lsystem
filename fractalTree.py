from TurtleWindow import TurtleWindow
from CommandType import CommandType

t = TurtleWindow()
t.turtle.stepLength=3
t.turtle.turningAngle=45

commands = {
  "G": (CommandType.DRAW_FORWARD,None),
  "[": [(CommandType.PUSH,None), (CommandType.ROTATE_LEFT,None)],
  "]": [(CommandType.POP,None), (CommandType.ROTATE_RIGHT,None)]
}
axiom = "G"
rules = {
  "F":"FF", 
  "G":"F[G]G"
}
t.show(
  axiom,
  rules,
  customCommands=commands,
  n=8,
  timeToDrawAllMs=1000
  )