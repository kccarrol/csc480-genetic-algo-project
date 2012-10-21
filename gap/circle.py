import math

class Circle:
   def __init__(self, position = (0.0, 0.0), radius = 1.0):
      self.position = position
      self.radius = radius

   def intersects(self, circle):
      distance = math.sqrt((self.position[0] - circle.position[0]) ** 2 \
                         + (self.position[1] - circle.position[1]) ** 2)
      return distance < self.radius + circle.radius

   def __str__(self):
      return "circle[%d, %d, %d]" % (self.position[0], self.position[1], self.radius)
