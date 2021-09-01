import unittest
from translator import *
class TestE2F(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(get_eng_to_french(" ")," " ) # test when nothing is given as input the output is nothing.
    def test2(self):
        self.assertEqual(get_eng_to_french("Hello"), "Bonjour")  # test when hello is given as input the output is bonjour
    def test3(self):
        self.assertNotEqual(get_eng_to_french("good"), "bonjour")  # test when good is given as input the output is not bonjour.
class TestF2E(unittest.TestCase): 
    def test4(self): 
        self.assertEqual(get_fr_to_english(" "), " ")# test when nothing is given as input the output is nothing.
    def test5(self):
        self.assertEqual(get_fr_to_english("Bonjour"), "Hello")  # test when bonjour is given as input the output is hello
    def test6(self):
        self.assertNotEqual(get_fr_to_english("bon"), "hello") # test when bon is given as input the output is not hello.


unittest.main()
