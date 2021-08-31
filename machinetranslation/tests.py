import unittest
from translator import *
class TestE2F(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench(" ")," " ) # test when nothing is given as input the output is nothing.
        self.assertEqual(englishToFrench("Hello"), "Bonjour")  # test when hello is given as input the output is bonjour
        self.assertNotEqual(englishToFrench("good"), "bonjour")  # test when good is given as input the output is not bonjour.
class TestF2E(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(frenchToEnglish(" "), " ")# test when nothing is given as input the output is nothing.
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")  # test when bonjour is given as input the output is hello
        self.assertNotEqual(frenchToEnglish("bon"), "hello") # test when bon is given as input the output is not hello.
unittest.main()
