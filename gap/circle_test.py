import unittest
from circle import Circle

class CircleTestCase(unittest.TestCase):
   def test_intersection(self):
      first = Circle()
      second = Circle((2.0, 0.0), 1.2)
      third = Circle((12.0, 0.0), 1.2)
      self.assertTrue(first.intersects(first))
      self.assertTrue(first.intersects(second))
      self.assertTrue(second.intersects(first))
      self.assertFalse(first.intersects(third))
      self.assertFalse(second.intersects(third))

if __name__ == '__main__':
   unittest.main()
