from lsystem import *

axiom = "F"
rules = {
  "F":"FfF", 
  "f":"fff"
}
show(
  rules,
  axiom,
  steps=2,
  n=6,
  start_pos=(0,400),
  start_rot=90,
  widthOfLine=3
  )