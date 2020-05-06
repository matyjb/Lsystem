# Lsystem
--------------------
## Posible commands

- push position and rotation on stack
- pop position and rotation from stack
- draw forward
- move forward
- rotate left by angle (in deg)
- rotate right by angle (in deg)

--------------------

## Default commands
'F' - draw forward by steps
'f' - move forward by steps
'+' - rotate right by angle
'-' - rotate left by angle
'[' - push state (position, rotation)
']' - pop state (position, rotation)

It is possible to pass custom commands in format of dictionary of
`<stringToIndicateCmd>: (<CommandType>,<argument>)`
or
`<stringToIndicateCmd>: [(<CommandType>,<argument>),(<CommandType>,<argument>)]`
If argument passed is None but it needs one then given command will take appropriately one of steps or angle as arguments
