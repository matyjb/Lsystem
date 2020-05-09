from TurtleWindow import TurtleWindow
from CommandType import CommandType

t = TurtleWindow()
t.turtle.stepLength=2
t.turtle.turningAngle=45
t.turtle.mulStep=1.36

axiom = "a"
rules = {
  "F":">F<",
  "a":"F[-x]Fb",
  "b":"F[+y]Fa",
  "x": "a",
  "y": "b",
}
t.show(
  axiom,
  rules,
  n=14,
  timeToDrawAllMs=1000
  )