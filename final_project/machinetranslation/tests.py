import unittest
from machinetranslation import translator

class testEnglishtoFrench(unittest.TestCase):
    def testEnglishtoFrench(self):
        self.assertIsNone(translator.english_to_french(''))
        self.assertEqual(translator.english_to_french('Hello'),'Bonjour')

class testFrenchToEnglish(unittest.TestCase):
    def testFrenchToEnglish(self):
        self.assertIsNone(translator.french_to_english(''))
        self.assertEqual(translator.french_to_english('Bonjour'),'Hello')