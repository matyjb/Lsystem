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
'#' - increment line width
'!' - decrement line width (line width >= 1)
'@' - draw a filled circle with line width as radius
'(' - decrement angle by one
')' - increment angle by one
'>' - multiply steps by steps multiply factor
'<' - divide steps by steps multiply factor

It is possible to pass custom commands in format of dictionary of
`<stringToIndicateCmd>: (<CommandType>,<argument>)`
or
`<stringToIndicateCmd>: [(<CommandType>,<argument>),(<CommandType>,<argument>)]`
If argument passed is None but it needs one then given command will take appropriately one of steps or angle as arguments

---------------------------------

You can take screenshots with F1 key
Screenshots are saved to screenshots folder in working directory