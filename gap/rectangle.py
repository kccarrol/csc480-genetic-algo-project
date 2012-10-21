class Rectangle:
   def __init__(self, x, y, w, h):
      self.x = x
      self.y = y
      self.w = w
      self.h = h

   def intersects_rect(self, other):
      return !(self.x + self.w < other.x \
            || self.x > other.x + other.w \
            || self.y + self.h < other.y \
            || self.y > other.y + other.h

   def intersects_circle(self, circle):
      # XXX
      return False
