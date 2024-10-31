import unittest
from piglatin import PigLatin
from error import PigLatinError

class TestPigLatin(unittest.TestCase):
    def test_get_phrase(self):
        translator = PigLatin("hello world")
        self.assertEqual(translator.get_phrase(), "hello world")

class TestPigLatin(unittest.TestCase):
    def test_get_phrase(self):
        translator = PigLatin("hello world")
        self.assertEqual(translator.get_phrase(), "hello world")
    def test_translate_empty_phrase(self):
        translator = PigLatin("")
        self.assertEqual(translator.translate(), "nil")
    
class TestPigLatin(unittest.TestCase):
   
    def test_translate_vowel_start_word(self):
        translator = PigLatin("any")
        self.assertEqual(translator.translate(), "anynay")

        translator = PigLatin("apple")
        self.assertEqual(translator.translate(), "appleyay")

       
        translator = PigLatin("ask")
        self.assertEqual(translator.translate(), "askay")
    
