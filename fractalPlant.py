from app.TurtleWindow import TurtleWindow

t = TurtleWindow()
t.turtle.stepLength = 2
t.turtle.turningAngle = 25

axiom = "X"
rules = {
    "X": "F+[[X]-X]-F[-FX]+X",
    "F": "FF",
}
t.show(
    axiom,
    rules,
    n=7,
    timeToDrawAllMs=50000,
)
