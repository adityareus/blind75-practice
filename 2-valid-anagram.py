"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false
Constraints:
s and t consist of lowercase English letters.
"""

"""Approach 1: Sorting"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_array = list(s)
        s_array.sort()
        t_array = list(t)
        t_array.sort()

        if (len(s_array) == len(t_array)):
            return s_array == t_array
        return False
    
"""Approach 2: sorted"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
    
"""Approach 3: Hash Map"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT