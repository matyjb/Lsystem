from app.CommandType import CommandType
from app.TurtleWindow import TurtleWindow

t = TurtleWindow()
t.turtle.stepLength = 10
t.turtle.turningAngle = 60

commands = {
    "G": (CommandType.DRAW_FORWARD, None),
}
axiom = "F"
rules = {
    "F": "F+G++G-F--FF-G+",
    "G": "-F+GG++G+F--F-G",
}
t.show(
    axiom,
    rules,
    customCommands=commands,
    n=4,
    timeToDrawAllMs=1000,
)
