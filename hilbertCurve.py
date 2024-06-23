from app.TurtleWindow import TurtleWindow

t = TurtleWindow()
t.turtle.stepLength = 10
t.turtle.turningAngle = 90

axiom = "A"
rules = {
    "A": "-BF+AFA+FB-",
    "B": "+AF-BFB-FA+",
}
t.show(
    axiom,
    rules,
    n=6,
    timeToDrawAllMs=1000,
)
