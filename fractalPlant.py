from lsystem import *

axiom = "X"
rules = {
  "X":"F+[[X]-X]-F[-FX]+X", 
  "F":"FF"
}
show(
  rules,
  axiom,
  steps=2,
  angle=25,
  n=7,
  start_pos=(10,800),
  start_rot=30,
  timeToDrawAllMs=50000
  )