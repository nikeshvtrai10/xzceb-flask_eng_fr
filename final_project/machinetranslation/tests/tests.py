import unittest

class TestEnglishToFrench(unittest.TestCase):
    def englishToFrench(self):
        self.assertEqual("","")
        self.assertEqual("Hello", "Bonjour")


class TestFrenchToEnglish(unittest.TestCase):
    def frenchToEnglish(self):
        self.assertEqual("", "")
        self.assertEqual("Bonjour", "Hello")
        
unittest.main()