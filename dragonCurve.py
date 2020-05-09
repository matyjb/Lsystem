from TurtleWindow import TurtleWindow
from CommandType import CommandType

t = TurtleWindow()
t.turtle.stepLength=5
t.turtle.turningAngle=90

axiom = "FX"
rules = {
  "X":"X+YF+", 
  "Y":"-FX-Y"
}
t.show(
  axiom,
  rules,
  n=12,
  timeToDrawAllMs=1000
  )