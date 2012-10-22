import unittest
from rectangle import Rectangle
from circle import Circle


class RectangleTest(unittest.TestCase):
   def test_circle_intersection(self):
      rect_one = Rectangle(0.0, 0.0, 2.0, 2.0)
      rect_two = Rectangle(8.0, 8.0, 10.0, 10.0)
      first_circ = Circle((2.0,2.0),1.2)
      sec_circ = Circle((12.0, 12.0), 2.2)

      self.assertTrue(rect_one.intersects_circle(first_circ)
      self.assertFalse(rect_one.intersects_circle(sec_circ)
 
      self.asserFalse(rect_two.intersects_circle(first_circ)
      self.assertTrue(rect_two.intersects_circle(sec_circ)
