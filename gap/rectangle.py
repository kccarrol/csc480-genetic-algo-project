import math

class Rectangle:
   def __init__(self, x, y, w, h):
      self.x = x
      self.y = y
      self.w = w
      self.h = h

   def intersects_rect(self, other):
      return not (self.x + self.w < other.x \
            or self.x > other.x + other.w \
            or self.y + self.h < other.y \
            or self.y > other.y + other.h)

   def closest(self, val, minimum, maximum):
      return max(minimum, min(val, maximum))

   def intersects_circle(self, circle):
      closeX = self.closest(circle.position[0], self.x, self.x+self.w)
      closeY = self.closest(circle.position[1], self.y, self.y+self.h)

      dX = circle.position[0] - closeX
      dY = circle.position[1] - closeY

      distance = math.sqrt((dX * dX) + (dY * dY))

      return distance < circle.radius


   def __str__(self):
      return "rectangle[%d, %d, %d, %d]" % (self.x, self.y, self.w, self.h)


