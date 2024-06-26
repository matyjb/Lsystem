import copy, time, os, pygame
from app.CommandType import *
from app.Turtle import *
from app.helperFunctions import *
pygame.init()

DRAWING_SURFACE_MARGIN = pygame.Vector2(5,5)
FONT_SIZE = 20
DRAWING_SURFACE_OFFSET = pygame.Vector2(0,20)

defaultCommands = {
  "F": (CommandType.DRAW_FORWARD,None),
  "f": (CommandType.MOVE_FORWARD,None),
  "[": (CommandType.PUSH,None),
  "]": (CommandType.POP,None),
  "-": (CommandType.ROTATE_LEFT,None),
  "+": (CommandType.ROTATE_RIGHT,None),
  "|": (CommandType.ROTATE_LEFT,180),
  "#": (CommandType.INC_LINE_WIDTH,None),
  "!": (CommandType.DEC_LINE_WIDTH,None),
  "@": (CommandType.DRAW_DOT,None),
  ")": (CommandType.INC_ANGLE,None),
  "(": (CommandType.DEC_ANGLE,None),
  ">": (CommandType.MUL_STEPS,None),
  "<": (CommandType.DIV_STEPS,None),
}

keys = {}

class TurtleWindow:
  def __init__(self,defaultTurtleState=None,maxRes=(800,800),minRes=(400,400)):
    turtleState=Turtle(pygame.Vector2(0,0),180,10,10,1,1,(255,255,255),1)
    if defaultTurtleState==None:
      self.turtle = copy.copy(turtleState)
    else:
      self.turtle = copy.copy(defaultTurtleState)
    self.defaultTurtleState = turtleState

    self.window = None
    self.maxRes = pygame.Vector2(maxRes)
    self.minRes = pygame.Vector2(minRes)
    self.uiSurface = None
    self.drawingSurface = None
    self.stack = []
    self.isRunning = False
    self.isAnimStopped = False
    self.executeNext = False

    # index of what command was last executed in each frame
    self.nextOperationIndexFloat = 0

    self.camPos = pygame.Vector2(0,0)

  def initWindow(self,res):
    self.window = pygame.display.set_mode(res)

  def initUISurface(self,res=None):
    if res == None:
      res = pygame.display.get_surface().get_size()
    self.uiSurface = pygame.Surface(res, pygame.SRCALPHA)
    self.uiSurface.fill((0,0,0,0))

  def initDrawingSurface(self,res=(800,800)):
    self.drawingSurface = pygame.Surface(res, pygame.SRCALPHA)
    self.drawingSurface.fill((0,0,0,0))

  def resetTurtleState(self):
    self.turtle = copy.copy(self.defaultTurtleState)
    self.stack = []

  def pushState(self,state=None):
    if state == None:
      self.stack.append(copy.copy(self.turtle))
    else:
      self.stack.append(state)

  def popState(self):
    self.turtle = self.stack.pop()

  def executeCommand(self,cmd,args=None,shouldDraw=True):
    if cmd == CommandType.MOVE_FORWARD:
      self.turtle.moveForward(args)

    elif cmd == CommandType.DRAW_FORWARD:
      oldPosition = self.turtle.position
      self.turtle.moveForward(args)
      newPosition = self.turtle.position
      if shouldDraw:
        pygame.draw.line(self.drawingSurface, self.turtle.color, oldPosition, newPosition, self.turtle.width)

    elif cmd == CommandType.ROTATE_LEFT:
      self.turtle.rotateLeft(args)

    elif cmd == CommandType.ROTATE_RIGHT:
      self.turtle.rotateRight(args)

    elif cmd == CommandType.PUSH:
      self.pushState(args)

    elif cmd == CommandType.POP:
      self.popState()

    elif cmd == CommandType.INC_LINE_WIDTH:
      if args == None:
        self.turtle.width += 1
      else:
        self.turtle.width += args

    elif cmd == CommandType.DEC_LINE_WIDTH:
      if args == None:
        self.turtle.width -= 1
      else:
        self.turtle.width -= args
        
      if self.turtle.width <= 0:
        self.turtle.width = 1

    elif cmd == CommandType.DRAW_DOT:
      if shouldDraw:
        pygame.draw.circle(self.drawingSurface, self.turtle.color, self.turtle.position, self.turtle.width if args is None else args)

    elif cmd == CommandType.INC_ANGLE:
      if args == None:
        self.turtle.turningAngle += 1
      else:
        self.turtle.turningAngle += args

    elif cmd == CommandType.DEC_ANGLE:
      if args == None:
        self.turtle.turningAngle -= 1
      else:
        self.turtle.turningAngle -= args

      if self.turtle.turningAngle <= 0:
        self.turtle.turningAngle = 1

    elif cmd == CommandType.MUL_STEPS:
      if args == None:
        self.turtle.stepLength *= self.turtle.mulStep
      else:
        self.turtle.stepLength *= args

    elif cmd == CommandType.DIV_STEPS:
      if args == None:
        self.turtle.stepLength /= float(self.turtle.mulStep)
      else:
        self.turtle.stepLength /= float(args)

    else:
      print("Unknown command: " + str(cmd))

  def exportDrawingSurfaceToFile(self):
    if not os.path.exists("./screenshots"):
      os.makedirs("./screenshots")
    timeTaken = time.asctime(time.localtime(time.time())).replace(" ","_").replace(":","-")
    saveFile = "screenshots/"+timeTaken+".png"
    pygame.image.save(self.drawingSurface,saveFile)
    print("Screenshot saved as " + saveFile)

  def handleEvents(self,dt):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.isRunning = False
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          self.isRunning = False
        if event.key == pygame.K_F1:
          self.exportDrawingSurfaceToFile()
        if  event.key in [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_t]:
          keys[event.key] = event
        if event.key == pygame.K_SPACE:
          self.isAnimStopped = not self.isAnimStopped
        if event.key == pygame.K_r:
          self.resetTurtleState()
          self.nextOperationIndexFloat = 0
          self.drawingSurface.fill((0,0,0,0))

      
      if event.type == pygame.KEYUP:
        if  event.key in [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_t]:
          del keys[event.key]
    
    if pygame.K_w in keys:
      self.camPos += pygame.Vector2(0,-1) * dt / 2.0
    if pygame.K_s in keys:
      self.camPos += pygame.Vector2(0,1) * dt / 2.0
    if pygame.K_a in keys:
      self.camPos += pygame.Vector2(-1,0) * dt / 2.0
    if pygame.K_d in keys:
      self.camPos += pygame.Vector2(1,0) * dt / 2.0
    if pygame.K_t in keys:
      self.executeNext = True

  def show(self,axiom="",rules={},customCommands={},n=0, timeToDrawAllMs=0, delay=1000, printString=False, drawTurtle=True):
    ##get final commands list
    commands = {k:v for (k,v) in defaultCommands.items()}
    for (key,val) in customCommands.items():
      commands[key] = val

    outputString = recursiveFindAndReplace(axiom,rules,n)
    if printString:
      print(outputString)
    print("String size: ",len(outputString))
    
    cmdsTodo = translateStringToCmds(commands,outputString)

    # calculate resolution for drawing based on cmdsTodo (progress turtle and check its position)
    self.pushState()
    maxX = minX = self.turtle.position.x
    maxY = minY = self.turtle.position.y
    for (c,a) in cmdsTodo:
      self.executeCommand(c,a,False)
      if maxX < self.turtle.position.x:
        maxX = self.turtle.position.x
      elif minX > self.turtle.position.x:
        minX = self.turtle.position.x

      if maxY < self.turtle.position.y:
        maxY = self.turtle.position.y
      elif minY > self.turtle.position.y:
        minY = self.turtle.position.y

    # and reset turtle back
    self.popState()
    self.stack = []

    topLeft = pygame.Vector2(minX,minY)
    bottomRight = pygame.Vector2(maxX,maxY)

    res = bottomRight - topLeft + DRAWING_SURFACE_MARGIN * 2
    fullRes = res + DRAWING_SURFACE_OFFSET
    if fullRes.x > self.maxRes.x:
      fullRes.x = self.maxRes.x
    if fullRes.y > self.maxRes.y:
      fullRes.y = self.maxRes.y

    if fullRes.x < self.minRes.x:
      fullRes.x = self.minRes.x
    if fullRes.y < self.minRes.y:
      fullRes.y = self.minRes.y
    ## init pygame stuff
    self.initWindow((int(fullRes.x),int(fullRes.y)))
    self.initUISurface()
    self.initDrawingSurface(res)
    self.turtle.position = self.turtle.position - topLeft + DRAWING_SURFACE_MARGIN
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(pygame.font.get_default_font(), FONT_SIZE)

    fromStart = 0 #how many ms elapsed from start
    ### MAIN LOOP
    self.isRunning = True
    self.defaultTurtleState = copy.copy(self.turtle)
    while self.isRunning:
      # CLEAR----------------------------------
      self.window.fill((0,0,0))
      self.uiSurface.fill((0,0,0,0))
      # TICKING--------------------------------
      dt = clock.tick()
      fromStart += dt
      # EVENTS---------------------------------
      self.handleEvents(dt)

      # UPDATE---------------------------------
      if delay < fromStart:
        if timeToDrawAllMs == 0:
          opsThisFrame = len(cmdsTodo)
        else:
          opsThisFrame = float(len(cmdsTodo)) / timeToDrawAllMs * dt

        if self.isAnimStopped:
          opsThisFrame = 0

        if self.executeNext:
          opsThisFrame += 1
          self.executeNext = False

        ## EXECUTE COMMANDS in this frame
        for (cmd, arg) in cmdsTodo[int(self.nextOperationIndexFloat):int(self.nextOperationIndexFloat + opsThisFrame)]:
          self.executeCommand(cmd,arg)

        ## progress in operations
        self.nextOperationIndexFloat += opsThisFrame
        if self.nextOperationIndexFloat >= len(cmdsTodo):
          self.nextOperationIndexFloat = len(cmdsTodo)
      
      # DRAWING--------------------------------
      # draw drawing surface on screen
      self.window.blit(self.drawingSurface, DRAWING_SURFACE_OFFSET+self.camPos)

      # generate progress text on screen
      opsOutOfAll = font.render(str(int(self.nextOperationIndexFloat))+" / "+str(len(cmdsTodo)), True, (255,255,255))
      self.uiSurface.blit(opsOutOfAll, (0, 0))

      # draw turle on screen too?
      if drawTurtle:
        # align with drawingSurface, draw, back to original position
        self.turtle.position += DRAWING_SURFACE_OFFSET
        self.turtle.draw(self.uiSurface, self.camPos)
        self.turtle.position -= DRAWING_SURFACE_OFFSET

      self.window.blit(self.uiSurface, (0,0))
      pygame.display.flip()


