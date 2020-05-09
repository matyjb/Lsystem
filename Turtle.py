import pygame

class Turtle:
  def __init__(self,position,rotation,turningAngle,stepLength,color,width):
    self.position = position
    self.rotation = rotation
    self.turningAngle = turningAngle
    self.stepLength = stepLength
    self.color = color
    self.width = width

  def draw(self,surface):
    scale = 6
    p0 = self.position + pygame.math.Vector2.rotate(pygame.Vector2(0,2) * scale, self.rotation)
    p1 = self.position + pygame.math.Vector2.rotate(pygame.Vector2(1,-1) * scale, self.rotation)
    p2 = self.position + pygame.math.Vector2.rotate(pygame.Vector2(-1,-1) * scale, self.rotation)
    pygame.draw.polygon(surface, self.color, (p0, p1, p2))
    pygame.draw.polygon(surface, (255,0,0), (p0, p1, p2), 1)