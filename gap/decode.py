import random

def main():
   print "--- Generate ---"
   s = generate(2)
   print "Return from generate function " + s
   #print "Enter your input"
   count = 0
   l =  len(s)
   while count < l:
      decode(s[count:count+41])
      count = count + 41

def decode(input):
   print len(input)
   signal = int(input[0])
   Xpos = convert(input[1:17])
   Ypos = convert(input[17:33])
   radius = convert(input[33:len(input)])
   print "On/off bit " + str(signal)
   print "X position " + str(Xpos)
   print "Y position " + str(Ypos)
   print "Radius " + str(radius)

def convert(s):
   count = 0
   l =  len(s)
   val = 0
   while count < l:
      if int(s[count]) == 1:
         val += 2**count
      count = count + 1
   return val

def generate(numberOfCircles):
   binary_string = ""
   for i in range(0,numberOfCircles):
      signal = str(random.randint(0,1))
      Xpos = binary_form(random.randint(0,65535),2)
      Ypos = binary_form(random.randint(0,65535),2)
      radius = binary_form(random.randint(0,255),1)
      #print "On/off bit " + signal
      #print "X position " + Xpos
      #print "Y position " + Ypos
      #print "Radius " + radius
      binary_string +=  signal + Xpos + Ypos + radius
      #print "Binary string " + binary_string + "  size " + str(len(binary_string))
   return binary_string
 
def binary_form(value, size):
   bVal =  bin(value)
   l = len(bVal)
   bVal = bVal[2:l]
   diff =  size*8 - (l - 2) 
   bVal =  ("0" * diff) + bVal 
   return bVal  
   
if __name__ == '__main__':
   main()
