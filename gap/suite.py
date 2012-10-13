import unittest
import circle_test

suite = unittest.TestLoader()
suite = suite.loadTestsFromModule(circle_test)

unittest.TextTestRunner().run(suite)
