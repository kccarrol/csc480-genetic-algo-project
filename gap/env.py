
class Env:

   def __init__(self, window, window_size, sf, envNum):
      self.window = window
      self.envNum = envNum
      self.sf = sf
      self.window_size = window_size
      self.createEnv(window, window_size, sf, envNum)

   def createEnv(self, window, window_size, sf, envNum):
      window.Draw(sf.Shape.Rectangle(0,0,window_size, window_size, sf.Color(255, 255, 255)))
      window.Draw(sf.String('Generation: 0'))

      #create the environment here
      if (envNum == 1):
         Env.env1(self, window, window_size, sf)
      if (envNum ==2):
         Env.env2(self, window, window_size, sf)


   def env1(self, window, window_size, sf):
      #Rectangle(X1, Y1, X2, Y2, Color, [Outline], [OutlineColor]);
      window.Draw(sf.Shape.Rectangle(0, 0, 30, 30, sf.Color(0,0,255)))
      window.Draw(sf.Shape.Rectangle(window_size-30,window_size-30 , window_size, window_size, sf.Color(255, 0, 0)))
      window.Draw(sf.Shape.Rectangle((window_size/2)-50, (window_size/2)-50, (window_size/2)+50, (window_size/2)+50, sf.Color(0,255,0)))
     
      
   def env2(self, window, window_size, sf):
      window.Draw(sf.Shape.Rectangle(100, 100, 200, 200, sf.Color(0,0,0)))
      window.Draw(sf.Shape.Rectangle((window_size/2)-100, (window_size/2)-100, (window_size/2)+100, (window_size/2)+100, sf.Color(0,0,0)))
