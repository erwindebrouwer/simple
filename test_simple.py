import unittest
from simple import Analyze_Number
#
class test_simple(unittest.TestCase):
    def test_Analyze_Number(self):
        self.assertEqual(Analyze_Number(100),"No way! That's exactly 100!")
        self.assertEqual(Analyze_Number(101),"Wow! That's higher than 100!")
        self.assertEqual(Analyze_Number(99),"Oops... That's lower than 100.")
