from lsystem import *

axiom = "a"
rules = {
  "F":">F<",
  "a":"F[-x]Fb",
  "b":"F[+y]Fa",
  "x": "a",
  "y": "b",
}
show(
  rules,
  axiom,
  steps=2,
  angle=45,
  start_pos=(400,800),
  n=14,
  stepsMulFactor=1.36,
  timeToDrawAllMs=1000
  )