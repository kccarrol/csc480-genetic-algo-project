from circle import Circle
import random

class Individual:
   def __init__(self):
      self.binary_string = ""

   def draw(self, window, env):
      fitness = self.fitness(env)
      for circle in self.decode():
         window.Draw(sf.Shape.Circle(circle.position[0], circle.position[1], circle.radius, sf.Color(100, 100, 0)))
      window.Draw(sf.String('Fitness: %' % fitness))

   def fitness(self, env):
      # XXX
      return 0

   def generate(self, number_of_circles):
      self.binary_string = ""
      for i in range(0,number_of_circles):
         signal = str(random.randint(0,1))
         Xpos = self._binary_form(random.randint(0,65535),2)
         Ypos = self._binary_form(random.randint(0,65535),2)
         radius = self._binary_form(random.randint(0,255),1)
         self.binary_string +=  signal + Xpos + Ypos + radius

   def decode(self):
      circle_size = 41
      circles = []
      for idx in range(0, len(self.binary_string), circle_size):
         input = self.binary_string[idx:idx+circle_size]
         signal = int(input[0])
         if signal:
            Xpos = self._convert(input[1:17]) / 65535.0 * 512
            Ypos = self._convert(input[17:33]) / 65535.0 * 512
            radius = self._convert(input[33:len(input)])
            circles.append(Circle((Xpos, Ypos), radius))
      return circles

   def _binary_form(self, value, size):
      bVal =  bin(value)
      l = len(bVal)
      bVal = bVal[2:l]
      diff =  size*8 - (l - 2) 
      bVal =  ("0" * diff) + bVal 
      return bVal  

   def _convert(self, s):
      count = 0
      l =  len(s)
      val = 0
      while count < l:
         if int(s[count]) == 1:
            val += 2**count
         count = count + 1
      return val

def random_individual():
   max_circles = 100
   individual = Individual()
   individual.generate(max_circles)
   return individual

def main():
   print "--- Generate ---"
   indiv = random_individual()
   print "Return from generate function " + indiv.binary_string
   circles = indiv.decode()
   for circle in circles:
      print circle
 
if __name__ == '__main__':
   main()
