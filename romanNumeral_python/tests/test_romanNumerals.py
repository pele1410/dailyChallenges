'''HACK to get the module on the path'''
import sys
sys.path.append(".")

from romanNumerals import compare_numerals 
import unittest

class TestNumerals(unittest.TestCase):
        def setUp(self):
                pass
        def tearDown(self):
                pass

        def test_valid_values(self):
                self.assertFalse (compare_numerals ("I", "I"))
                self.assertTrue (compare_numerals ("I", "II"))
                self.assertFalse (compare_numerals ("II", "I"))
                self.assertFalse (compare_numerals ("V", "IIII"))
                self.assertFalse (compare_numerals ("V", "IV"))
                self.assertTrue (compare_numerals ("MDCLXV","MDCLXVI"))
                self.assertFalse (compare_numerals ("MM","MDCCCCLXXXXVIIII"))
                self.assertTrue (compare_numerals ("IX","X"))
                self.assertTrue (compare_numerals ("X","CIX"))

        def test_empty_Input(self):
                self.assertRaises (ValueError, compare_numerals, "I", "")
                self.assertRaises (ValueError, compare_numerals, "", "I")
                self.assertRaises (ValueError, compare_numerals, "", "")

        def test_invalid_numerals(self):
                self.assertRaises (KeyError, compare_numerals, "2", "1")
                self.assertRaises (KeyError, compare_numerals, "I", "I1")
                self.assertRaises (KeyError, compare_numerals, "LKI", "I")
                self.assertRaises (KeyError, compare_numerals, "L I", "I")

        def test_invalid_sequence(self):
                self.assertRaises (RuntimeError, compare_numerals, "ID", "D")
                self.assertRaises (RuntimeError, compare_numerals, "VX", "X")
                self.assertRaises (RuntimeError, compare_numerals, "IL", "X")
                self.assertRaises (RuntimeError, compare_numerals, "CCCIIX", "X")

if __name__ == "__main__":
        unittest.main()