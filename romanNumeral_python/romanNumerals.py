#!/usr/bin/env python


'''
@brief Challenge to compare Roman Numerals values

Source:
https://www.reddit.com/r/dailyprogrammer/comments/oe9qnb/20210705_challenge_397_easy_roman_numeral/

For the purpose of today's challenge, a Roman numeral is a non-empty string of the characters M, D, C, L, X, V, and I, each of which has the value 1000, 500, 100, 50, 10, 5, and 1. The characters are arranged in descending order, and the total value of the numeral is the sum of the values of its characters. For example, the numeral MDCCXXVIIII has the value 1000 + 500 + 2x100 + 2x10 + 5 + 4x1 = 1729.

This challenge uses only additive notation for roman numerals. There's also subtractive notation, where 9 would be written as IX. You don't need to handle subtractive notation (but you can if you want to, as an optional bonus).

Given two Roman numerals, return whether the first one is less than the second one:

numcompare("I", "I") => false
numcompare("I", "II") => true
numcompare("II", "I") => false
numcompare("V", "IIII") => false
numcompare("MDCLXV", "MDCLXVI") => true
numcompare("MM", "MDCCCCLXXXXVIIII") => false
You only need to correctly handle the case where there are at most 1 each of D, L, and V, and at most 4 each of C, X, and I. You don't need to validate the input, but you can if you want. Any behavior for invalid inputs like numcompare("V", "IIIIIIIIII") is fine - true, false, or error.
'''

import unittest

def numeral_values ():
        return {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}

def is_subtraction_valid(left_value_, right_value_, last_letters_):
        '''
        Subtraction of numerals is only valid when:
        1) The numeral on the left of the pair is one of I, X, or C
        2) The numeral on the left is not more than 10x less than the numeral on the right.
           e.g. IX is valid, IC is not
        3) There are not two consecutive lower values to the left of a right value
           e.g. CIX is valid, IIX is not
        '''
        if right_value_ > left_value_ * 10:
                return False

        if len(last_letters_) == 2 and last_letters_[0] == last_letters_[1]:
                return False

        return right_value_/ left_value_ == 10 or right_value_ / left_value_ == 5

def numeral_to_int(numeral_):
        if not numeral_:
                raise ValueError ("Empty numeral input")

        sum = 0
        dict = numeral_values();
        last_value = 999999
        last_letters = ""
        for letter in numeral_:
                new_value = dict[letter]
                if new_value <= last_value:
                        sum += new_value
                elif is_subtraction_valid(last_value, new_value, last_letters):
                        sum -= last_value
                        sum += new_value - last_value
                else:
                        message = "Invalid consectutive numerals:"+last_letters+letter
                        print(message)
                        raise RuntimeError(message)
                        
                last_value = new_value
                last_letters = last_letters[-1:] + letter

        return sum

def compare_numerals (numeral1_, numeral2_):
        int1 = numeral_to_int(numeral1_)
        int2 = numeral_to_int(numeral2_)

        return int1<int2

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
                '''This case is not handled'''
                self.assertRaises (RuntimeError, compare_numerals, "CCCIIX", "X")

if __name__ == "__main__":
        unittest.main()