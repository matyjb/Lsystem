from lsystem import *

axiom = "A"
rules = {
  "A":"-BF+AFA+FB-", 
  "B":"+AF-BFB-FA+"
}
show(
  rules,
  axiom,
  steps=10,
  angle=90,
  n=6,
  start_pos=(0,799),
  timeToDrawAllMs=1000
  )