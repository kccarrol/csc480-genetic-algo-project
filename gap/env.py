from PySFML import *
from rectangle import Rectangle

class Env:
   def __init__(self, window_size):
      self.env_num = 1
      self.window_size = window_size
      self.create_env1()

   def draw(self, window):
      for obstacle in self.obstacles:
         window.Draw(sf.Shape.Rectangle(obstacle.x, obstacle.y, obstacle.w, obstacle.h, sf.Color(0, 0, 255)))

   def create_env1(self):
      self.obstacles = []
      self.obstacles.append(Rectangle(0, 0, 30, 30))
      self.obstacles.append(Rectangle(self.window_size - 30, self.window_size - 30, self.window_size, self.window_size))
      self.obstacles.append(Rectangle(self.window_size / 2 - 50, self.window_size / 2 + 50, self.window_size / 2 + 50, self.window_size / 2 + 50))

   def create_env2(self):
      self.obstacles = []
      self.obstacles.append(Rectangle(100, 100, 200, 200))
      self.obstacles.append(Rectangle(self.window_size / 2 - 100, self.window_size / 2 - 100, self.window_size / 2 + 100, self.window_size / 2 + 100))
