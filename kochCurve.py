from lsystem import *

axiom = "F"
rules = {
  "F":"F-F+F+F-F"
}
show(
  rules,
  axiom,
  steps=10,
  angle=90,
  n=3,
  opPerSec=2000
  )