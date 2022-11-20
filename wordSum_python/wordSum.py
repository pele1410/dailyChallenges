#!/usr/bin/env python

'''
 @brief Challenge to build up sums of words based on character values

 Source:
 https://www.reddit.com/r/dailyprogrammer/comments/onfehl/20210719_challenge_399_easy_letter_value_sum/

 Challenge
 Assign every lowercase letter a value, from 1 for a to 26 for z. Given a string of
 lowercase letters, find the sum of the values of the letters in the string.

 lettersum("") => 0
 lettersum("a") => 1
 lettersum("z") => 26
 lettersum("cab") => 6
 lettersum("excellent") => 100
 lettersum("microspectrophotometries") => 317
 Optional bonus challenges
 Use the enable1 word list for the optional bonus challenges.

 microspectrophotometries is the only word with a letter sum of 317. Find the only word with
 a letter sum of 319.

 How many words have an odd letter sum?

 There are 1921 words with a letter sum of 100, making it the second most common letter sum.
 What letter sum is most common, and how many words have it?

 zyzzyva and biodegradabilities have the same letter sum as each other (151), and their
 lengths differ by 11 letters. Find the other pair of words with the same letter sum whose
 lengths differ by 11 letters.

 cytotoxicity and unreservedness have the same letter sum as each other (188), and they have
 no letters in common. Find a pair of words that have no letters in common, and that have
 the same letter sum, which is larger than 188. (There are two such pairs, and one word
 appears in both pairs.)

 The list of word { geographically, eavesdropper, woodworker, oxymorons } contains 4 words.
 Each word in the list has both a different number of letters, and a different letter sum.
 The list is sorted both in descending order of word length, and ascending order of letter
 sum. What's the longest such list you can find?
 '''

import os.path
import sys

def dictionary ():
        DICTIONARY_FILE = "words.txt"

        if not os.path.isfile(DICTIONARY_FILE):
                print('Dictionary file does not exist:', DICTIONARY_FILE)
                return {}
        else:
                with open(DICTIONARY_FILE) as f:
                        lines = f.read().splitlines()
        
        return lines

def letterValue (letter_):
        return ord(letter_.lower())-96

def wordSum(word_):
        sum = 0
        for letter in word_:
                sum += letterValue(letter)

        return sum

def findWordsWithSum(sum_):
        for line in dictionary ():
                sum = wordSum(line)
                if sum == sum_:
                        print(line,"has sum of", sum_)

def printMaxSum():
        allSums = {}
        for line in dictionary ():
                sum = wordSum(line)
                newSum = allSums.get(sum,0)
                allSums[sum] = newSum+1

        maxSum = -1
        maxSums = []
        for sum in allSums.keys():
                if allSums[sum] >= maxSum:
                        maxSum = allSums[sum]
                        maxSums.append(sum)

        for sum in maxSums:
                print("Sum of",sum,"has max sum of", maxSum)

def printAllSums():
        for line in dictionary ():
                sum = wordSum(line)
                print(line,"has sum of", sum)



# Main loop
argc = len(sys.argv)

try:
        if sys.argv[1] == "all":
                printAllSums()
        elif sys.argv[1] == "max":
                printMaxSum()
        elif sys.argv[1] == "sum":
                try:
                        findWordsWithSum(int(sys.argv[2]))
                except ValueError:
                        print("Invalid input, please try again")
except IndexError:
        print("Missing required arguments")

