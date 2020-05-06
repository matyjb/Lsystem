from lsystem import *

axiom = "FX"
rules = {
  "X":"X+YF+", 
  "Y":"-FX-Y"
}
show(
  rules,
  axiom,
  steps=5,
  angle=90,
  n=12,
  msPerLine=2
  )