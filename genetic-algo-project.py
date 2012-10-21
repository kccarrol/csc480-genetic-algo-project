from PySFML import *
import random
import time
import threading
import gap

def main() :
   window_size = 640
   window = sf.RenderWindow(sf.VideoMode(window_size, window_size), "CSC-480: Circle Plotting with Genetic Algorithms")

   env = gap.Env(window_size)
   population = gap.Population(env)

   #define start Time
   initialTime = time.clock()

   while True:
      event = sf.Event()
      while window.GetEvent(event):
         if event.Type == sf.Event.Closed:
            return
         if ((event.Type == sf.Event.KeyPressed) and (event.Key.Code == sf.Key.Q)):
            return
         if ((event.Type == sf.Event.KeyPressed) and (event.Key.Code == 49)): # 49 is Num1 
            env.create_env1()
         if ((event.Type == sf.Event.KeyPressed) and (event.Key.Code == 50)): # 50 is Num2
            env.create_env2()

      window.Draw(sf.Shape.Rectangle(0, 0, window_size, window_size, sf.Color(0, 0, 0)))
      env.draw(window)
      population.draw(window)
      window.Draw(sf.String('Generation: 0'))
      window.Display()

      currentTime = time.clock()

      if ((currentTime - initialTime) > 2):
         initialTime = currentTime
         numCircles += 1

if __name__ == '__main__':
   main()
