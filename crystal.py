from lsystem import *

axiom = "F-F-F-F"
rules = {
  "F":"FF-F--F-F", 
}
show(
  rules,
  axiom,
  steps=5,
  angle=90,
  n=4,
  msPerLine=2,
  start_pos=(0,799)
  )