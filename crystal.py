from app.TurtleWindow import TurtleWindow

t = TurtleWindow()
t.turtle.stepLength = 5
t.turtle.turningAngle = 90

axiom = "F-F-F-F"
rules = {
    "F": "FF-F--F-F",
}
t.show(
    axiom,
    rules,
    n=4,
    timeToDrawAllMs=1000,
)
