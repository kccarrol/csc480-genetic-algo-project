from individual import *

class Population:
   max_members = 100
   members = []

   def __init__(self, env):
      self.env = env
      for idx in range(0, self.max_members):
         members.append(random_individual())
      self.sort()

   def draw(self, window):
      self.members[0].draw(window, self.env)

   def sort(self):
      self.members = sorted(self.members, key = lambda member: member.fitness(self.env))
