
import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_e2f_hello(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
    def test_e2f_name(self):
        self.assertEqual(english_to_french('My name is Tom.'),'Je m\'appelle Tom.')

class TestFrenchToEnglish(unittest.TestCase):
    def test_f2e_bonjour(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
    def test_f2e_day(self):
        self.assertEqual(french_to_english('Jour'),'Day')
    def test_f2e_notequal(self):
        self.assertNotEqual(french_to_english('Vous'),'Me')

unittest.main()