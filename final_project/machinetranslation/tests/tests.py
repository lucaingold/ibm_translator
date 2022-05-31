"""Import files"""
import unittest
from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    def testFrenchtoEnglish(self):
        self.assertEqual(french_to_english(''), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def testEnglishtoFrench(self):
        self.assertEqual(english_to_french(''), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

if __name__ == "__main__":
    unittest.main()