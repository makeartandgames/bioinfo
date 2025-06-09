import unittest
from bioinfo import translators 
class TranslatorsTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_distance_is_hamming_or_levenshtein(self):
      a = "kitten"
      b = "settin"
      dist = translators.compare_sequences(a, b, {})[-1]
      self.assertEqual(dist, 3)

    def test_distance_is_hamming_not_levenshtein(self):
      a = "abcdef"
      b =  "bcdefg"
      dist = translators.compare_sequences(a, b, {})[-1]
      # hamming distance will give 6, not 2
      self.assertEqual(dist, 6)

#def test_distance_is_levenshtein(self):
#      a = "abcdef"
#      b =  "bcdefg"
#      dist = translators.compare_sequences(a, b, {})[-1]
#      # hamming distance will give 6, not 2
#      self.assertEqual(dist, 2)
#
#    def test_distance_is_not_hamming(self):
#      a = "abcdef"
#      b =  "bcdefg"
#      dist = translators.compare_sequences(a, b, {})[-1]
#      # hamming distance will give 6, not 2
#      self.assertNotEqual(dist, 6)
#

if __name__ == "__main__":
    unittest.main()
