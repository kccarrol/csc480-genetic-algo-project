from PySFML import *
import random
import time
import threading
import gap

def main() :
   window_size = 640
   window = sf.RenderWindow(sf.VideoMode(window_size, window_size), "CSC-480: Circle Plotting with Genetic Algorithms")

   #define start Time
   initialTime = time.clock()

   # Create the initial population list (array)
   population = []
   numCircles = 0

   # Assign a random radious between 0 and 200. Populates our list
   # Assigns a random x and y coordinate for our population
   for i in range(0,99):
      circle = gap.Circle((random.randrange(0,window_size), random.randrange(0,window_size)), random.randrange(0,200))
      population.append(circle)

   while True:
      event = sf.Event()
      while window.GetEvent(event):
         if event.Type == sf.Event.Closed:
            return

      window.Draw(sf.Shape.Rectangle(0, 0, window_size, window_size, sf.Color(0, 0, 0)))
      window.Draw(sf.String('Generation: 0'))
      window.Draw(sf.Shape.Circle(window_size / 2, window_size / 2, 100, sf.Color(100, 0, 0)))
      drawCircles(window, population, numCircles)
      window.Display()

      currentTime = time.clock()

      if ((currentTime - initialTime) > 2):
         initialTime = currentTime
         numCircles += 1

def drawCircles(window, population, size) :
   for idx in range(0, size):
      circle = population[idx]
      window.Draw(sf.Shape.Circle(circle.position[0], circle.position[1], circle.radius, sf.Color(0,100,100)))

if __name__ == '__main__':
   main()
