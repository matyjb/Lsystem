from TurtleWindow import TurtleWindow
from CommandType import CommandType

t = TurtleWindow()
t.turtle.stepLength=2
t.turtle.width=3

axiom = "F"
rules = {
  "F":"FfF", 
  "f":"fff"
}
t.show(
  axiom,
  rules,
  n=7,
  timeToDrawAllMs=1000
  )