from pygame import *

class Turtle:
  def __init__(self,position,rotation,turningAngle,stepLength,mulStep,mulAngle,color,width):
    self.position = position
    self.rotation = rotation
    self.turningAngle = turningAngle
    self.stepLength = stepLength
    self.mulStep = mulStep
    self.mulAngle = mulAngle
    self.color = color
    self.width = width

  def moveForward(self,by=None):
    if by == None:
      by = self.stepLength
    self.position = math.Vector2.rotate(Vector2(0,by), self.rotation) + self.position

  def rotateLeft(self,degrees=None):
    if degrees == None:
      degrees = self.turningAngle
    self.rotation += degrees

    if self.rotation > 180:
      self.rotation -= 360

  def rotateRight(self,degrees=None):
    if degrees == None:
      degrees = self.turningAngle
    self.rotation -= degrees

    if self.rotation < -180:
      self.rotation += 360

  def draw(self,surface,offset=Vector2(0,0)):
    scale = 6
    p0 = self.position + math.Vector2.rotate(Vector2(0,2) * scale, self.rotation) + offset
    p1 = self.position + math.Vector2.rotate(Vector2(1,-1) * scale, self.rotation) + offset
    p2 = self.position + math.Vector2.rotate(Vector2(-1,-1) * scale, self.rotation) + offset
    draw.polygon(surface, self.color, (p0, p1, p2))
    draw.polygon(surface, (255,0,0), (p0, p1, p2), 1)