from app.TurtleWindow import TurtleWindow

t = TurtleWindow()
t.turtle.stepLength = 10
t.turtle.turningAngle = 90

axiom = "F"
rules = {
    "F": "F-F+F+F-F",
}
t.show(
    axiom,
    rules,
    n=3,
    timeToDrawAllMs=2000,
)
