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
    "F": "G+F+G",
    "G": "F-G-F",
}
t.show(
    axiom,
    rules,
    customCommands=commands,
    n=6,
    timeToDrawAllMs=1000,
)
